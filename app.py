from flask import Flask, request, jsonify

app = Flask(__name__)

# Data structure to store website visits
website_visits = {}


# Endpoint to track a visit to a website by a specific customer using a specific device


@app.route('/visit_website', methods=['POST'])
def visit_website():
    data = request.json
    customer_id = data.get('customerId')
    device_id = data.get('deviceId')
    website_id = data.get('websiteId')

    # Ensure each customer visit is counted only once, regardless of the device used
    if customer_id in website_visits:
        if device_id not in website_visits[customer_id]:
            website_visits[customer_id].add(device_id)
    else:
        website_visits[customer_id] = {device_id}

    return jsonify({'message': 'Visit tracked successfully.'}), 200


# Endpoint to retrieve the number of visits a specific customer has made to a specific website
@app.route('/get_website_visit_count_for_customer', methods=['GET'])
def get_website_visit_count_for_customer():
    customer_id = request.args.get('customerId')
    website_id = request.args.get('websiteId')

    if customer_id in website_visits:
        visit_count = len(website_visits[customer_id])
    else:
        visit_count = 0

    return jsonify({'customerId': customer_id, 'websiteId': website_id, 'visitCount': visit_count}), 200


# Endpoint to retrieve the total number of visits to a specific website by all customers
@app.route('/get_overall_website_hit_count', methods=['GET'])
def get_overall_website_hit_count():
    website_id = request.args.get('websiteId')

    overall_visit_count = sum(len(devices) for devices in website_visits.values())

    return jsonify({'websiteId': website_id, 'overallHitCount': overall_visit_count}), 200


if __name__ == '__main__':
    app.run(debug=True)