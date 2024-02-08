import tkinter as tk
import datetime
import locale
locale.setlocale(locale.LC_CTYPE, 'en_US.UTF-8')

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")  # Đặt tiêu đề cho cửa sổ

        # Thời gian cần đếm ngược đến (năm, tháng, ngày, giờ, phút, giây)
        target_time = datetime.datetime(2032, 1, 1, 0, 0, 0)

        # Tính toán thời gian còn lại
        self.remaining_time = target_time - datetime.datetime.now()

        # Tạo các thành phần giao diện
        self.label = tk.Label(root, font=("Helvetica", 16))
        self.label.pack(expand=True, fill='both')

        self.update_timer()

        # Bind sự kiện thay đổi kích thước cửa sổ với hàm cập nhật kích thước chữ
        self.root.bind("<Configure>", self.update_font_size)

        self.root.minsize(500, 300)

    def update_timer(self):
        # Kiểm tra xem thời gian đã hết chưa
        if self.remaining_time.total_seconds() <= 0:
            self.label.config(text="End up")
        else:
            # Cập nhật thời gian còn lại
            self.remaining_time = self.remaining_time - datetime.timedelta(seconds=1)

            # Chuyển đổi timedelta thành datetime cụ thể
            delta_date = datetime.datetime(1, 1, 1) + self.remaining_time

            # Hiển thị thời gian còn lại với định dạng giây đứng đầu
            formatted_time = delta_date.strftime("còn %S giây %M phút %H giờ %d ngày %m tháng %Y năm")
            self.label.config(text=formatted_time)

            # Gọi lại hàm cập nhật sau 1000ms (1 giây)
            self.root.after(1000, self.update_timer)

    def update_font_size(self, event):
        # Cập nhật kích thước chữ để chữ luôn nằm giữa màn hình và phóng to khi thay đổi kích thước cửa sổ
        new_font_size = max(6, int(event.width / 34))  # Đặt kích thước tối thiểu là 16
        self.label.config(font=("Helvetica", new_font_size))


if __name__ == "__main__":
    root = tk.Tk()  # Khởi tạo một đối tượng Tkinter
    app = CountdownApp(root)  # Tạo một đối tượng của ứng dụng Countdown
    root.mainloop()  # Bắt đầu vòng lặp chính của Tkinter
