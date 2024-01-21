def generate_html(product_types):
    html_output = '<div class="swiper-container">\n    <div class="swiper-wrapper">\n'

    for product_type in product_types:
        for product in product_type['products']:
            html_output += f'''
        <!-- Slide for {product['name']} -->
        <div class="swiper-slide">
            <div class="container">
                <div class="image-section">
                    <img src="{product['image']}" alt="{product['name']}">
                    <div class="button-container">'''

            # Add print button options
            if 'print_options' in product:
                html_output += '\n                        <select onchange="downloadFile(this.value, this)">\n                            <option value="">Print</option>\n'
                for group_label, options in product['print_options'].items():
                    html_output += f'                            <optgroup label="{group_label}">\n'
                    for option in options:
                        html_output += f'                                <option value="{option['link']}">{option['label']}</option>\n'
                    html_output += '                            </optgroup>\n'
                html_output += '                        </select>\n'

            # Add buy button
            if 'cost' in product:
                html_output += f'''                        <button onclick="addToCart('{product['name']}', {product['cost']}, '{product['stripe_id']}', this.closest('.swiper-slide').querySelector('.image-section img'))">Buy</button>\n'''

            html_output += f'''                    </div>
                <div class="hidden-section" id="{product['section_id']}">
                    <h2>{product['name']}</h2>
                    <div class="video-wrapper">
                        <video id="video-{product['section_id']}" muted loop controls>
                            <source src="{product['video_src']}" type="video/mp4">
                        </video>
                        <iframe src="{product['iframe_src']}" title="YouTube video player" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <p>{product['description']}</p>
                    <div class="link-container">'''

            # Add additional links
            for link in product['links']:
                html_output += f'''                        <button class="link-button" onclick="window.open('{link['url']}')">{link['label']}</button>\n'''

            html_output += '''                    </div>
                </div>
            </div>
        </div>'''

    html_output += '''
    </div>

    <!-- Pagination & Navigation -->
    <div class="swiper-pagination"></div>
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>
</div>'''

    return html_output

# Example data
product_types = [
    {
        'type': 'slider',
        'products': [
            {
                'name': 'Yuki',
                'image': 'static\\images\\classic.webp',
                'print_options': {
                    'Prusa': [
                        {'label': 'Mini', 'link': 'https://example.com/yuki-prusa-mini.zip'},
                        {'label': 'MK3S/MK4', 'link': 'https://example.com/yuki-prusa-mk3s.zip'}
                    ]
                    # Add other printer options...
                },
                'cost': 17.90,
                'stripe_id': 'price_1Oaf48AuFwBMux61hD5gCa7E',
                'video_src': 'https://example.com/yuki_video.mp4',
                'iframe_src': 'https://www.youtube.com/embed/vF2obkSBFAg',
                'description': 'Fits any 80mm PC fan',
                'links': [
                    {'label': 'Thingiverse', 'url': 'https://www.thingiverse.com/riverfamily/designs'},
                    {'label': 'Printables', 'url': 'https://www.printables.com/model/217636-yuki-air-cooler'}
                ],
                'section_id': 'section1-1'
            }
            # Add other products...
        ]
    }
    # Add other product types...
]

# Generate HTML
html_code = generate_html(product_types)
print(html_code)