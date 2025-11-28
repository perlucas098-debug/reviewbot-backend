from flask import Flask, request, jsonify
from review_generator import generate_review
from amazon_parser import extract_product_info
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    product_url = data.get('url')
    affiliate_tag = data.get('affiliate_tag', '')

    product_info = extract_product_info(product_url)
    review = generate_review(product_info['title'])

    affiliate_link = product_url
    if affiliate_tag:
        separator = '&' if '?' in product_url else '?'
        affiliate_link = f"{product_url}{separator}tag={affiliate_tag}"

    return jsonify({
        'title': product_info['title'],
        'price': product_info.get('price', 'No disponible'),
        'review': review,
        'affiliate_link': affiliate_link
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
