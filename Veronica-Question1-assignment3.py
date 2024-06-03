import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube

# Encapsulation: Combining data and methods into a single unit (class).
class YouTubeDownloaderApp(tk.Tk):
    """Main application class for YouTube Downloader."""
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.geometry("400x200")
        self.initialize_ui()

    def initialize_ui(self):
        """Initialize the main frame of the application."""
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

# Abstraction: Hide intricate implementation details and exposing only the relevant pieces.
class MainFrame(tk.Frame):
    """Main frame containing the widgets for downloading videos."""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        """Create and layout the widgets."""
        self.url_label = ttk.Label(self, text="YouTube URL:")
        self.url_label.pack(pady=10)

        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.pack(pady=5)

        self.download_button = ttk.Button(self, text="Download", command=self.download_video)
        self.download_button.pack(pady=20)

    def download_video(self):
        """Download the highest resolution video from the provided URL."""
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Warning", "Enter a valid YouTube URL")
            return

        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            messagebox.showinfo("Success", f"Downloaded: {yt.title}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download: {e}")

# Inheritance and Polymorphism: MainFrame is inherited and extended.
class CustomMainFrame(MainFrame):
    """Customized main frame to download only audio streams."""
    def __init__(self, parent):
        super().__init__(parent)

    def download_video(self):
        """Download only the audio from the provided URL."""
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Warning", "Enter a valid YouTube URL")
            return

        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            stream.download()
            messagebox.showinfo("Success", f"Downloaded (Audio Only): {yt.title}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download: {e}")

# Multiple Inheritance: Combining features from various classes.
class ExtendedMainFrame(CustomMainFrame, MainFrame):
    """Extended frame demonstrating multiple inheritance."""
    def __init__(self, parent):
        super().__init__(parent)

    @classmethod
    def class_method_example(cls):
        """Example class method."""
        return "This is a class method."

    @staticmethod
    def static_method_example():
        """Example static method."""
        return "This is a static method."

if __name__ == "__main__":
    app = YouTubeDownloaderApp()
    
    # Changing the frame to an extended one using encapsulated data.
    app.main_frame.destroy()
    app.main_frame = ExtendedMainFrame(app)
    app.main_frame.pack(fill=tk.BOTH, expand=True)

    # Displaying the use of class and static methods.
    print(ExtendedMainFrame.class_method_example())
    print(ExtendedMainFrame.static_method_example())

    app.mainloop()
