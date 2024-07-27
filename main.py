from flask import Flask, render_template, request
from flask_caching import Cache
from flask_compress import Compress


app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "simple"})  # Simple in-memory cache
Compress(app)


global_content = {
    "experience": "21",
}

home_content = {
    "hero": {
        "title": "Trust Your Wealth With The Insurance Specialist",
        "subtitle": "When you trust your health only with a specialist, why not your wealth? We are Zeal, your insurance specialist.",
        "content": "Zeal Direct & Reinsurance Broking Services is licensed, regulated and controlled by the Insurance Regulatory and Development Authority (IRDA), the insurance regulatory body in India. We are also a member of the Insurance Brokers Association of India.",
        "number": "012 345 6789",
    },
    "stats": {
        "happy_clients": "3000",
        "projects_succeed": "3000",
        "awards_achieved": "50",
        "team_members": "250",
        "heading": "For Individuals And Organisations",
        "content": "We analyze the comprehensive needs of our clients and offer end-to-end solutions for insurance, risk management and reinsurance in all classes of business.",
    },
    "whyus": {
        "title": "Few Reasons Why People Choose Us!",
        "content": "At Zeal, we stand at the forefront of the global risk, insurance, and reinsurance landscape, driven by a mission to redefine professionalism and excellence. By identifying and addressing our clients' specific needs with research-based solutions at competitive prices, we ensure maximum shareholder wealth through efficient resource management. Choose Zeal for trusted expertise, innovative solutions, and a commitment to shaping a secure future for all.",
    },
    "carousel": {
        "items": [
            {
                "title": "Tailored Insurance Solutions",
                "content": "Our team of experts analyzes your unique needs and creates a customized insurance plan that fits your specific requirements.",
                "image": "/static/img/carousel-1.jpg",
            },
            {
                "title": "Global Network of Partners",
                "content": "We have access to a vast network of reputable insurers and reinsurers worldwide, ensuring you get the best coverage options.",
                "image": "/static/img/carousel-2.jpg",
            },
        ]
    },
    "services": {
        "items": [
            {
                "title": "Life Insurance",
                "content": "Group & Individual Life Products",
                "image": "/static/img/icon/icon-10-light.png",
            },
            {
                "title": "Health Insurance",
                "content": "Motor, Health and Personal Accident",
                "image": "/static/img/icon/icon-01-light.png",
            },
            {
                "title": "Home Insurance",
                "content": "Fire and Loss of profits",
                "image": "/static/img/icon/icon-05-light.png",
            },
            {
                "title": "Vehicle Insurance",
                "content": "Motor, Health and Personal Accident",
                "image": "/static/img/icon/icon-08-light.png",
            },
            {
                "title": "Business Insurance",
                "content": "Construction & Engineering Sectors, Oil and Energy Sectors, Liability and WC, Group & Individual Life Products, Credit and Financial Lines, Aviation",
                "image": "/static/img/icon/icon-07-light.png",
            },
            {
                "title": "Property Insurance",
                "content": "Fire and Loss of profits, Construction & Engineering Sectors, Oil and Energy Sectors, Marine Cargo and Hull, Liability and WC",
                "image": "/static/img/icon/icon-06-light.png",
            },
        ]
    },
    "appointment": {
        "title": "We're Award Winning Insurance Company",
        "content": "Zeal Direct & Reinsurance Broking Services is licensed, regulated and controlled by the Insurance Regulatory and Development Authority (IRDA), the insurance regulatory body in India. We are also a member of the Insurance Brokers Association of India.",
        "number": "+91 944 356 4555",
    },
    "team": {
        "title": "Meet Our Professional Team Members",
        "members": [
            {
                "name": "Avani Sharma",
                "designation": "Chief Risk Officer",
                "image": "/static/img/team-1.jpg",
                "linkedin": "https://www.linkedin.com/in/avani-sharma",
                "twitter": "https://twitter.com/avani_sharma",
                "facebook": "https://facebook.com/avani.sharma",
                "youtube": "https://youtube.com/avani.sharma",
            },
            {
                "name": "Rahul Desai",
                "designation": "Senior Insurance Analyst",
                "image": "/static/img/team-2.jpg",
                "linkedin": "https://www.linkedin.com/in/rahul-desai",
                "twitter": "https://twitter.com/rahul_desai",
                "facebook": "https://facebook.com/rahul.desai",
                "youtube": "https://youtube.com/rahul.desai",
            },
            {
                "name": "Priya Kapoor",
                "designation": "Reinsurance Specialist",
                "image": "/static/img/team-3.jpg",
                "linkedin": "https://www.linkedin.com/in/priya-kapoor",
                "twitter": "https://twitter.com/priya_kapoor",
                "facebook": "https://facebook.com/priya.kapoor",
                "youtube": "https://youtube.com/priya.kapoor",
            },
            {
                "name": "Vijay Singh",
                "designation": "Insurance Consultant",
                "image": "/static/img/team-4.jpg",
                "linkedin": "https://www.linkedin.com/in/vijay-singh",
                "twitter": "https://twitter.com/vijay_singh",
                "facebook": "https://facebook.com/vijay.singh",
                "youtube": "https://youtube.com/vijay.singh",
            },
        ],
    },
    "testimonial": {
        "title": "What They Say About Our Insurance",
        "testimonials": [
            {
                "name": "Rajesh Kumar",
                "designation": "CEO, Tech Solutions",
                "image": "/static/img/testimonial-1.jpg",
                "content": "“Zeal has been a true partner in helping us navigate the complex world of insurance. Their expertise and personalized approach have given us peace of mind, knowing our business is well-protected.”",
            },
            {
                "name": "Anjali Patel",
                "designation": "Business Owner, Retail",
                "image": "/static/img/testimonial-2.jpg",
                "content": "“I was impressed by Zeal's ability to explain insurance in a clear and concise manner. They found the right coverage for my needs and have been incredibly responsive whenever I had a question.”",
            },
            {
                "name": "Sandeep Singh",
                "designation": "Financial Advisor",
                "image": "/static/img/testimonial-3.jpg",
                "content": "“Zeal's commitment to their clients is evident in everything they do. They go above and beyond to ensure their customers have the best possible experience. I highly recommend them to anyone looking for insurance solutions.”",
            },
        ],
    },
}

about_content = {}

service_content = {}


# testing base template
@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/")
def index():
    return render_template(
        "index.html",
        home_content=home_content,
        global_content=global_content,
        enumerate=enumerate,
    )


@app.route("/about")
def about():
    return render_template(
        "about.html", about_content=about_content, global_content=global_content
    )


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/admin/<page>")
def admin(page):
    return render_template("admin.html", page=page, home_content=home_content)


if __name__ == "__main__":
    app.run(debug=True)
