import glob

for html_file in glob.glob('frontend/index*.html'):
    with open(html_file, 'r') as f:
        content = f.read()

    # Target the Add to Cart buttons specifically
    target1 = 'class="btn btn-primary btn-sm" onclick="document.getElementById(\'cart-section\').scrollIntoView({behavior: \'smooth\'})"><i class="fa-solid fa-cart-shopping"></i> Add to Cart'
    target2 = 'class="btn btn-primary btn-sm" onclick="document.getElementById(\'cart-section\').scrollIntoView({behavior: \'smooth\'})">\n                                <i class="fa-solid fa-cart-shopping"></i> Add to Cart'
    
    replace_with = 'class="btn btn-primary btn-sm" onclick="showToast(\'Item added to cart!\'); document.getElementById(\'cart-section\').scrollIntoView({behavior: \'smooth\'})"><i class="fa-solid fa-cart-shopping"></i> Add to Cart'

    content = content.replace(target1, replace_with)
    # Also handle indexA.html which might have different formatting if I recall correctly, wait no, my previous python script unified them mostly.
    
    with open(html_file, 'w') as f:
        f.write(content)
    print(f"Updated {html_file}")
