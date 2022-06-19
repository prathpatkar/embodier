import embodier

img = embodier.AvatarGenerator().BlockAvatar()
img.show()

img = embodier.AvatarGenerator().BlockAvatar(xy_axis=11,pixels=300,background_color='lightgrey',border=True,border_width=25)
img.show()

img = embodier.AvatarGenerator().TextAvatar("PT")
img.show()