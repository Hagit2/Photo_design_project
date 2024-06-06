from PIL import Image
import cv2
import imageio


class image:
    def __init__(self, name_window, pass_image):
        self.name_window = name_window
        self.pass_image = pass_image
        self.action = None
        self.ix = -1
        self.iy = -1
        self.direction_image = -1
        self.txt = "None"
        self.img = imageio.imread(pass_image)
        self.save_img = imageio.imread(pass_image)
        self.path_to_save = None
        width = 700
        height = 400
        resized_image = cv2.resize(self.img, (width, height))
        self.img = resized_image
        self.filename = None
        self.show()

    def show(self):
        if self.img is not None and self.img.shape[0] > 0 and self.img.shape[1] > 0:
            cv2.imshow(self.name_window, self.img)
            self.mouse()

    def mouse(self):
        if (self.action == 'cut'):
            cv2.setMouseCallback(self.name_window, self.cut_image)
        elif (self.action == 'add_circle'):
            cv2.setMouseCallback(self.name_window, self.add_circle)
        elif (self.action == 'add_rectangle'):
            cv2.setMouseCallback(self.name_window, self.add_rectangle)
        elif (self.action == 'add_line'):
            cv2.setMouseCallback(self.name_window, self.add_line)
        elif (self.action == 'first_image'):
            self.first_img()
        elif (self.action == 'add_frame'):
            self.migration()
        elif (self.action == 'add_txt'):
            cv2.setMouseCallback(self.img, self.add_text)
        elif (self.action == 'save'):
            self.save()
        else:
            cv2.setMouseCallback(self.name_window, lambda *args: None)

    def set_action(self, action):
        self.action = action
        self.mouse()


    def set_txt(self, txt):
       self.txt = txt

    def add_text(self,event, x, y, flags, param):
        font=cv2.FONT_HERSHEY_SIMPLEX
        if event == cv2.EVENT_LBUTTONDOWN:
            text_to_add=self.txt
            if text_to_add is not None:
                cv2.putText(self.img, text_to_add, (x, y), font, 1.0, (0, 255, 0), 2)
                cv2.imshow(self.name_window, self.img)

    def add_rectangle(self, event, x, y, flags, param):
        global ix, iy
        if event == cv2.EVENT_LBUTTONDOWN:
            ix = x
            iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            cv2.rectangle(self.img, (ix, iy), (x, y), (0, 40, 0), 5, cv2.FILLED)
            cv2.imshow(self.name_window, self.img)

    def add_line(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            cv2.line(self.img, (self.ix, self.iy), (x, y), (120, 150, 0), 5, cv2.FILLED)
            cv2.imshow(self.name_window, self.img)

    def add_circle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self.img, (x, y), 50, (0, 255, 0), -1)
            cv2.imshow(self.name_window, self.img)

    def set_direction(self, direction):
        self.direction_image = direction
        self.direction(self.direction_image)

    def direction(self, direction):
        if direction == 1:
            self.img = cv2.rotate(self.img, cv2.ROTATE_180)
        elif direction == -1:
            self.img = cv2.rotate(self.img, cv2.ROTATE_90_CLOCKWISE)
        elif direction == -2:
            self.img = cv2.rotate(self.img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow(self.name_window, self.img)

    def first_img(self):
        self.img = self.save_img
        cv2.imshow(self.name_window, self.img)

    def migration(self):
        frame_thickness = 20
        frame_color = (182, 82, 180)
        self.img = cv2.copyMakeBorder(self.img, frame_thickness, frame_thickness, frame_thickness,
                                      frame_thickness, cv2.BORDER_CONSTANT, value=frame_color)
        cv2.imshow(self.name_window, self.img)

    def cut_image(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            x1, x2 = sorted([self.ix, x])
            y1, y2 = sorted([self.iy, y])
            cropped_image = self.img[y1:y2, x1:x2]
            self.img = cropped_image
            self.show()

    def befor_save_img(self,path):
        self.path_to_save=path
        self.save_img()

    def save_img(self):

        pil_img = Image.fromarray(self.__img)
        pil_img.save(self.path_to_save)

    def save(self):
        cv2.imwrite(self.filename, self.img)


    def set_filename(self , filename):
        self.filename=filename
        self.action= "save"
        self.mouse()

