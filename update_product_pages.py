import os
import re

# Product data for structured data
products = {
    "2fhd0620": {
        "name": "Firstack 2FHD0620 SiC Gate Driver",
        "description": "A dual-channel plug-and-play gate driver optimized for up to 1700V SiC MOSFET modules in EconoDUAL™ packages.",
        "image": "https://firstack-distributor.com/images/products/firstack-2fhd0620.jpg",
        "price": "499"
    },
    "2fhd0320c": {
        "name": "Firstack 2FHD0320C IGBT Driver",
        "description": "A highly reliable dual-channel plug-and-play gate driver for 1200V and 1700V IGBT modules in PrimePACK™ 3/3+ packages.",
        "image": "https://firstack-distributor.com/images/products/firstack-2fhd0320c.jpg",
        "price": "449"
    },
    "2fhd0115c": {
        "name": "Firstack 2FHD0115C IGBT Driver",
        "description": "Cost-effective and reliable dual-channel driver for IGBT modules in EconoDUAL™ packages.",
        "image": "https://firstack-distributor.com/images/products/firstack-2fhd0115c.jpg",
        "price": "399"
    },
    "2fhc0215": {
        "name": "Firstack 2FHC0215 Driver Core",
        "description": "High-performance dual-channel IGBT driver core with reinforced insulation for custom PCB designs.",
        "image": "https://firstack-distributor.com/images/products/firstack-2fhc0215.jpg",
        "price": "299"
    },
    "2fsc0110": {
        "name": "Firstack 2FSC0110 SiC Driver Core",
        "description": "Compact dual-channel driver core optimized for SiC MOSFETs for custom PCB designs.",
        "image": "https://firstack-distributor.com/images/products/firstack-2fsc0110.jpg",
        "price": "279"
    }
}

def update_product_page(file_path, product_id):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add canonical tag
    canonical_url = f"https://firstack-distributor.com/products/{'gate-drivers' if 'gate-drivers' in file_path else 'driver-cores'}/{product_id}.html"
    canonical_tag = f'<link rel="canonical" href="{canonical_url}">'
    
    # Add structured data
    product_data = products.get(product_id, {})
    if product_data:
        structured_data = f'''<script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Product",
      "name": "{product_data['name']}",
      "image": "{product_data['image']}",
      "description": "{product_data['description']}",
      "brand": {{
        "@type": "Brand",
        "name": "Firstack"
      }},
      "offers": {{
        "@type": "Offer",
        "priceCurrency": "USD",
        "price": "{product_data['price']}",
        "availability": "https://schema.org/InStock",
        "seller": {{
          "@type": "Organization",
          "name": "LiTong - Authorized Firstack Distributor"
        }}
      }}
    }}
    </script>'''
        
        # Update the head section
        content = re.sub(
            r'(<head>\s*<meta[^>]+>\s*<meta[^>]+>\s*<title>[^<]+</title>\s*)(<meta[^>]+>)?\s*<link rel="stylesheet"',
            f'\\1{canonical_tag}\n    {structured_data}\n    <link rel="stylesheet"',
            content,
            flags=re.DOTALL
        )
        
        # Write updated content back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {file_path}")

# Process all product files
for root, dirs, files in os.walk("products"):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            product_id = file.replace(".html", "")
            update_product_page(file_path, product_id)

print("All product pages updated successfully!")