import imageio.v3 as iio

filenames = ['Python programs/codedex/GIF project/team-pic1.png', 'Python programs/codedex/GIF project/team-pic2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('Python programs/codedex/GIF project/team.gif', images, duration = 500, loop = 0)