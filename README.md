# codeyad course downloader

ربات دانلود خودکار دوره های کدیاد.
دانلود خودکار قسمت به قسمت و خروجی json به همراه ، کلیک خودکار دکمه مشاهده کردم هر قسمت.

دانلود خودکار لینک های استخراج شده به ترتیب و پوشه بندی و عدد گذاری خودکار هر قسمت.
برای مثال برای هر فصل یک پوشه به همون نام ایجاد و قسمت های اون فصل در اون پوشه قرار می گیرند.

## Installation

```bash
pip install selenium
pip install webdriver_manager
```

## Usage

```bash
python3 main.py
enter username: Your codeyad Username
enter password: your codeyad Password
enter course_url: your Course Url
```
پس از اتمام فایل main.py اطلاعات در فایل json ذخیره می شوند ، سپس فایل download.py ران می کنیم تا اطلاعات از فایل json دریافت و دانلود انجام بدهد.
```bash
python3 download.py
```
خودکار تمامی فایل های json دریافت ، و دانلود را انجام می دهد.
