from SimpleCV import *
import time
import os

pwd = os.getcwd()

numero_foto = 0
numero_collage = 0
cam = Camera()
threshold = 4.0

previa = cam.getImage()

while True:
	time.sleep(0.5)
	actual = cam.getImage()
	diferencia = actual - previa
	matriu = diferencia.getNumpy()
	mean = matriu.mean()

	diferencia.show()

	if mean >= threshold:
		print "Moviment Detectat"
		actual.save(pwd + "/motion/" + str(numero_collage) + "/foto" + str(numero_foto) + ".jpg")
		numero_foto = numero_foto + 1

		if numero_foto >= 10:
			img0 = Image(pwd + "/motion/" + str(numero_collage) + "/foto0.jpg").resize(320,240)
			img1 = Image(pwd + "/motion/" + str(numero_collage) + "/foto1.jpg").resize(320,240)
			img2 = Image(pwd + "/motion/" + str(numero_collage) + "/foto2.jpg").resize(320,240)
			img3 = Image(pwd + "/motion/" + str(numero_collage) + "/foto3.jpg").resize(320,240)
			img4 = Image(pwd + "/motion/" + str(numero_collage) + "/foto4.jpg").resize(320,240)
			img5 = Image(pwd + "/motion/" + str(numero_collage) + "/foto5.jpg").resize(320,240)
			img6 = Image(pwd + "/motion/" + str(numero_collage) + "/foto6.jpg").resize(320,240)
			img7 = Image(pwd + "/motion/" + str(numero_collage) + "/foto7.jpg").resize(320,240)
			img8 = Image(pwd + "/motion/" + str(numero_collage) + "/foto8.jpg").resize(320,240)
			img9 = Image(pwd + "/motion/" + str(numero_collage) + "/foto9.jpg").resize(320,240)

			filera0 = img0.sideBySide(img1)
			filera1 = img2.sideBySide(img3)
			filera2 = img4.sideBySide(img5)
			filera3 = img6.sideBySide(img7)
			filera4 = img8.sideBySide(img9)

			collage = filera0.sideBySide(filera1, side="bottom").sideBySide(filera2, side="bottom").sideBySide(filera3, side="bottom").sideBySide(filera4, side="bottom")
			collage.save(pwd + "/motion/" + str(numero_collage) + "/collage" + str(numero_collage) + ".jpg")

			numero_foto = 0
			numero_collage = numero_collage + 1
			if numero_collage >= 20:
				numero_collage = 0
	previa = actual
