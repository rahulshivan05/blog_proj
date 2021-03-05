from django.db import models
from users.models import CustomUser
import random
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw



class Code(models.Model):
	number = models.CharField(max_length=5, blank=True)
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	qr_code = models.ImageField(upload_to='Codes/', blank=True)

	def __str__(self):
		return str(self.number)

	def save(self, *args, **kwargs):
		number_list = [x for x in range(10)]
		code_items = []

		for i in range(5):
			num = random.choice(number_list)
			code_items.append(num)
		code_string = "".join(str(items) for items in code_items)
		self.number = code_string

		# Generating QrCode for User Code
		qrcode_img = qrcode.make(self.number)
		canvas = Image.new('RGB', (290, 290), 'white')
		draw = ImageDraw.Draw(canvas)
		canvas.paste(qrcode_img)
		fname = f'qr_code-{self.user}.png'
		buffer = BytesIO()
		canvas.save(buffer, 'PNG')
		self.qr_code.save(fname, File(buffer), save=False)
		canvas.close()

		super().save(*args, **kwargs)
