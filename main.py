from PIL import Image
import os
import random

#escAld = Image.open("escudos/aldosivi.png")
#escArs = Image.open("escudos/arsenal.png")
#pAld = escAld.load()
#pArs = escArs.load()

def is_red(c):
	if c[0] > 159:
		if c[1] < 60 and c[2] < 60:
			return True
	return False
def is_green(c):
	if c[1] > 159:
		if c[0] < 60 and c[2] < 60:
			return True
	return False
def is_blue(c):
	if c[2] > 159:
		if c[1] < 60 and c[0] < 60:
			return True
	return False

def is_yellow(c):
	if c[0] > 170 and c[1] > 170 and c[2] < 10:
			return True
	return False

def take_second(e):
	return e[1]


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
	
	most_colors.sort(key=take_second, reverse=True)
	
	c = [x for x in most_colors if x[0] != (0,0,0,0)]

	#if len(c) > 1:
	return c
	#else:
	#	most_colors = [(x, colors[x]) for x in colors if colors[x] > 250]
	
	#	most_colors.sort(key=take_second, reverse=True)
	
	#	return [x for x in most_colors if x[0] != (0,0,0,0)]

#aldo_cols = extract_main_colors(escAld)
#ars_cols = extract_main_colors(escArs)

def cols_mas_menos_parecidos(c1, c2):
	permi = 30
	rmax, rmin = c2[0] + permi, c2[0] - permi
	gmax, gmin = c2[1] + permi, c2[1] - permi
	bmax, bmin = c2[2] + permi, c2[2] - permi

	if (c1[0] < rmax and c1[0] > rmin) and (c1[1] < gmax and c1[1] > gmin) and (c1[2] < bmax and c1[2] > bmin):
		return True

	return False



def change_cols(esc, col, new_col):
	p = esc.load()
	
	alr_change = 0
	for i in range(esc.size[0]):
		for j in range(esc.size[1]):	
			#if p[i,j] == col[0][0]: 
			#	p[i,j] = new_col[0][0]
			if cols_mas_menos_parecidos(p[i,j], col[0][0]): 
				p[i,j] = new_col[0][0]

	for i in range(esc.size[0]):
		for j in range(esc.size[1]):	
			#if p[i,j] == col[1][0]: 
			if cols_mas_menos_parecidos(p[i,j], col[1][0]): 
				p[i,j] = new_col[1][0]

def change_cols_two_imgs(im1, im2):
	col1 = extract_main_colors(im1)
	col2 = extract_main_colors(im2)

	change_cols(im1, col1, col2)

def two_random_mash():
	base_dir = "escudos_arg/"	
	fls = os.listdir("./"+base_dir)
	eq1 = random.randint(0,len(fls)-1)
	eq2 = random.randint(0,len(fls)-1)
	print("equipo1: {}\nequipo2: {}".format(fls[eq1],fls[eq2]))
	esc1 = Image.open("escudos_arg/"+fls[eq1])
	esc2 = Image.open("escudos_arg/"+fls[eq2])
	change_cols_two_imgs(esc1,esc2)
	esc1.show()

#change_cols(escArs, ars_cols, aldo_cols)
#change_cols(escAld, aldo_cols, ars_cols)


# paiting red pixels to blue
#for i in range(escAld.size[0]):
#	for j in range(escAld.size[1]):
#		if is_yellow(pAld[i,j]):
#			pAld[i,j] = (255,0,0)