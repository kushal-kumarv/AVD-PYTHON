import cv2
import numpy as np

canvas = np.zeros((600, 800, 3), dtype=np.uint8)
palette_height = 60
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255),
    (0, 0, 0),
]
current_color = colors[0]
drawing = False
ix = iy = -1


def draw_palette(display_image):
    for i, color in enumerate(colors):
        x0 = 10 + i * 95
        y0 = 10
        x1 = x0 + 70
        y1 = palette_height - 10
        cv2.rectangle(display_image, (x0, y0), (x1, y1), color, -1)
        cv2.rectangle(display_image, (x0, y0), (x1, y1), (255, 255, 255), 2)

    selected_index = colors.index(current_color)
    sx0 = 10 + selected_index * 95
    cv2.rectangle(display_image, (sx0, 8), (sx0 + 70, palette_height - 8), (255, 255, 255), 3)


def refresh_window():
    display = canvas.copy()
    draw_palette(display)
    cv2.imshow("Draw Interface", display)


def draw_rectangle(event, x, y, flags, param):
    global drawing, ix, iy, canvas, current_color

    if y < palette_height:
        if event == cv2.EVENT_LBUTTONDOWN:
            index = (x - 10) // 95
            if 0 <= index < len(colors):
                current_color = colors[index]
                refresh_window()
        return

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = canvas.copy()
            draw_palette(temp_img)
            cv2.rectangle(temp_img, (ix, iy), (x, y), current_color, 2)
            cv2.imshow("Draw Interface", temp_img)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(canvas, (ix, iy), (x, y), current_color, 2)
        refresh_window()


cv2.namedWindow("Draw Interface")
cv2.setMouseCallback("Draw Interface", draw_rectangle)

while True:
    refresh_window()
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
    elif key == ord('c'):
        canvas[:] = 0

cv2.destroyAllWindows()