class Camera:
	def __init__(self, pixel, multi):
		self.pixel = pixel
		self.multi = multi
	def takepicture(self):
		print("찰칵")
		print("사진이 저장되었습니다.(화소:%d만, 배율:%.1fx)" % (self.pixel, self.multi))

if __name__ == "__main__":
	canon = Camera(2430, 1.0)
	canon.takepicture()
	sony = Camera(2410, 3.0)
	sony.takepicture()
