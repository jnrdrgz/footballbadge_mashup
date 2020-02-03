from PIL import Image
import os
import random
import sys

def extract_main_colors(im):
	p = im.load()

	colors = {}
	for i in range(im.size[0]):
		for j in range(im.size[1]):
			if p[i,j] in colors.keys():
				colors[p[i,j]] += 1
			else:
				colors[p[i,j]] = 1

	most_colors = [(x, colors[x]) for x in colors if colors[x] > 3000]
	
	most_colors.sort(key=lambda x : x[1], reverse=True)
	
	c = [x for x in most_colors if x[0][3] != 0]

	p = "escudos/primera/"
	if(im.filename == p+"river.png" or im.filename == p+"argentinos.png"):
		c[2], c[1] = c[1], c[2]
	
	return c
	
def cols_mas_menos_parecidos(c1, c2):
	permi = 30
	rmax, rmin = c2[0] + permi, c2[0] - permi
	gmax, gmin = c2[1] + permi, c2[1] - permi
	bmax, bmin = c2[2] + permi, c2[2] - permi

	if(c1[3] == 0 or c2[3] == 0):
		return False

	if (c1[0] < rmax and c1[0] > rmin) and (c1[1] < gmax and c1[1] > gmin) and (c1[2] < bmax and c1[2] > bmin):
		return True

	return False

def change_cols(esc, col, new_col):
	p = esc.load()
	
	alr_change = 0
	for i in range(esc.size[0]):
		for j in range(esc.size[1]):	
			f=False
			if cols_mas_menos_parecidos(p[i,j], col[0][0]): 
				p[i,j] = new_col[0][0]
				f=True
			if not f:
				if cols_mas_menos_parecidos(p[i,j], col[1][0]): 
					p[i,j] = new_col[1][0]

def change_cols_two_imgs(im1, im2):
	col1 = extract_main_colors(im1)
	col2 = extract_main_colors(im2)

	change_cols(im1, col1, col2)

def name_creator(eq1,eq2):
	if "-" in eq1:
		eq1 = eq1.split("-")[0]
	if "-" in eq2:
		eq2 = eq2.split("-")[0]
	n = "{}{}".format(eq1[:len(eq1)//2], eq2[len(eq2)//2:])
	return n

def test_main_colors(e):
	im = Image.open("escudos/primera/{}.png".format(e))

	print(extract_main_colors(im))

def two_mash(ran=False, eq1=None,eq2=None):
	base_dir = "escudos/primera/"	
	if ran:
		
		fls = os.listdir("./"+base_dir)
		eq1 = random.randint(0,len(fls)-1)
		eq2 = random.randint(0,len(fls)-1)
		print("equipo1: {}\nequipo2: {}".format(fls[eq1],fls[eq2]))
		print("forman: {}".format(name_creator(fls[eq1].replace(".png",""), fls[eq2].replace(".png",""))))
		esc1 = Image.open(base_dir+fls[eq1])
		esc2 = Image.open(base_dir+fls[eq2])
		change_cols_two_imgs(esc1,esc2)
		
		esc1.save('out.png')
	else:
		eq1 = eq1+".png"
		eq2 = eq2+".png"
		
		print("equipo1: {}\nequipo2: {}".format(eq1,eq2))
		print("forman: {}".format(name_creator(eq1.replace(".png",""), eq2.replace(".png",""))))
		
		esc1 = Image.open(base_dir+eq1)
		esc2 = Image.open(base_dir+eq2)
		change_cols_two_imgs(esc1,esc2)

		esc1.save('out.png')

if __name__ == '__main__':
	if len(sys.argv) == 3:
		if sys.argv[1] == "-tc":
			test_main_colors(sys.argv[2])
		else:
			two_mash(False, sys.argv[1], sys.argv[2]) 
	else:
		two_mash(True)