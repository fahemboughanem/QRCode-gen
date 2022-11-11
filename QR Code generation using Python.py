{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "edc5492f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pyqrcode in /usr/lib/python3/dist-packages (1.2.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pyqrcode\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "95b6c408",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter anything to generate QR : https://www.facebook.com/profile.php?id=100084415895689\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAPUAAAD1AQAAAACgyo7IAAADGklEQVR4nO1ZQY6kOBCMLJDMnlzSPMB8pKD6WSXRgm5GmjftaXH9YH7gesBIyc1IFLEH98yxtqSVaB86LwjiEKF0OjJthHgUy+EhDHzhX/j/xGcROczlrfJS3ip/fKvh5VVEZMhCH3pywqWde+0wn4Hb0iscqTvx/xd+lwoofHXFd2e9FsG82wFy2Iv/UZQfT1s6nNwisbK/ytjaXzvxP6sPQKwwcml+/mC1HYad+J/BC0bMA9Dqva5Eu9vyogC3XPS9iZxxqe07APM+v7bmHbiJHDPQB6bQntwsyckOzmzo0+eYg74VxmsRIuxIQ4WLDQBO6D9f3wGYTcDJLS0aXOrlbFdUAFCJ7sP/OEjtYLx2jtQ+GM8VpPY0m81gfQ+ANYwnV2IRVwKn4w9WPALLeSf+x0Fq5yAKoOXgYoM+IHlOJvUHwGx2RQRws17fak52karZj/9BpDFAtCckVd0YDLUIsc3BXw4A4LhZqc0/rsTyokC84lLvyP8oyGR9AyLsyChaBAjHkI3/2dfW8kbaaR5QNehcPMlSy3kn/sdBauc4oXMQjjQTikCvcCab/kaSWgRudnWx5YAkt9UM1jftX+MVoNeCJFMlBk459A+QZDDkiihcYUjSbIBDk8P+SP2XXjtnvBYE7IDYKpBP/a1poIptcuXVcUuTVi75c8ZrH+g5BnquiC0ZouSQvwOAwscGcKAMTs4oWPF4r6tmHvLwPyAKR0I4gNNH/TlmMf8l/zMbOpgNBQ21c2ZDEWKTg74SmI/gVb9xeeG9jrAl5jPglqvdgf+p9XWxQQfAMkThCjR2hdmy8T/32/V60nMkqQB9Dvv3w1+YskZC0uuAmE3/6AN9ElSEKFwdAMDkkr80v8ABdiRgydigZx79N+1fyMZbLXqv4196L83f53sN4Q78T60v6TmGKBxAT4Z0Ps9iPjgg3Z/OS4sGRUCD76iueBP44078T+FFqCirkwMuLWDHMPe34fP1/bl/Acxk1z9D1oBs7l9QMMKOAc1saCY7wEzzh8lkkT8AQiaRsdU+HYeRxfwnX/8Hv/BPxP8FSOZSZSUgMGcAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<PIL.PngImagePlugin.PngImageFile image mode=1 size=245x245>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pyqrcode\n",
    "from PIL import Image\n",
    "link= input (\"Enter anything to generate QR : \")\n",
    "qr_code= pyqrcode.create(link)\n",
    "qr_code.png(\"QRCode.png\", scale=5)\n",
    "Image.open(\"QRCode.png\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a1f2d58",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
