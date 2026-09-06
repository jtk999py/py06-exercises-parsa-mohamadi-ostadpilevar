# BARNAME FOROSHGAH MOSHTARI

x = input ('salam aya mikhahid kharid konid ? ')
y = x.lower()
n = y.strip()
products = []
if n == 'yes':
    p = input('esm mahsool ra vared konid : ')
    products.append(p)
    print(f'mahsool{products} be sabad kharid add shod')
elif n == 'no':
    print('mamnoon')
else:
    print('faghat ba yes ba no javab bedahid')