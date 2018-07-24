from passlib.hash import md5_crypt

h = md5_crypt.hash("password")
print h

md5_crypt.verify("password", h)

md5_crypt.verify("secret", h)

md5_crypt.using(salt_size=4).hash("password")