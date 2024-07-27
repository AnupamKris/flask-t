from flask import Flask, render_template, request
from flask_caching import Cache
from flask_compress import Compress


app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "simple"})  # Simple in-memory cache
Compress(app)


global_content = {"experience": "21", "number": "+91 944 356 4555"}

home_content = {
    "hero": {
        "title": "Zeal Insurance: Your Trusted Partner for Risk Management and Insurance Solutions",
        "subtitle": "Experience the difference of working with an insurance specialist.",
        "content": "Zeal Insurance is a leading provider of risk, insurance, and reinsurance solutions globally, managed by seasoned professionals with strong connections to domestic and international insurance markets. We are licensed by the Insurance Regulatory and Development Authority (IRDA) and a member of the Insurance Brokers Association of India.",
        "number": "+91 44 42117075",
    },
    "stats": {
        "happy_clients": "3000",
        "projects_succeed": "3000",
        "awards_achieved": "50",
        "team_members": "250",
        "heading": "For Individuals and Businesses",
        "content": "We analyze the comprehensive needs of our clients and offer end-to-end solutions for insurance, risk management and reinsurance in all classes of business.",
    },
    "whyus": {
        "title": "Why Choose Zeal Insurance?",
        "content": "We are committed to redefining professionalism and excellence in the insurance industry. Our core values of professionalism, trust, commitment, good corporate citizenship, ethics, and innovation drive us to deliver exceptional service and client-centric solutions. We prioritize understanding our clients' needs and challenges to provide research-based solutions at competitive prices while maximizing shareholder wealth through efficient resource utilization.",
    },
    "carousel": {
        "items": [
            {
                "title": "Tailored Risk Management Solutions",
                "content": "Our Risk Management Group provides comprehensive services including insurance portfolio audits, gap analysis reports, risk inspections, claims management, and enterprise risk management strategies. We work closely with clients to identify and mitigate potential risks, ensuring optimal protection.",
                "image": "/static/img/carousel-1.jpg",
            },
            {
                "title": "Diverse Insurance Coverage",
                "content": "Our General Insurance Group offers a wide range of insurance products covering various sectors, including construction & engineering, fire & LOP, motor, marine cargo & hull, credit & financial, oil & energy, group & individual life, and health & PA insurance. We provide customized solutions to meet your specific needs and industry requirements.",
                "image": "/static/img/carousel-2.jpg",
            },
        ]
    },
    "services": {
        "items": [
            {
                "title": "Life Insurance",
                "content": "Provides financial protection to individuals and groups in case of death or critical illness.",
                "image": "/static/img/icon/icon-10-light.png",
            },
            {
                "title": "Health Insurance",
                "content": "Covers medical expenses and personal accident-related costs.",
                "image": "/static/img/icon/icon-01-light.png",
            },
            {
                "title": "Fire and LOP Insurance",
                "content": "Protects against fire damage and losses related to business interruption.",
                "image": "/static/img/icon/icon-05-light.png",
            },
            {
                "title": "Motor Insurance",
                "content": "Covers damage to vehicles, personal injury, and third-party liability.",
                "image": "/static/img/icon/icon-08-light.png",
            },
            {
                "title": "Business Insurance",
                "content": "Offers specialized insurance for various sectors like construction, energy, and liability.",
                "image": "/static/img/icon/icon-07-light.png",
            },
            {
                "title": "Property Insurance",
                "content": "Provides comprehensive coverage for various types of property, including buildings, contents, and marine cargo.",
                "image": "/static/img/icon/icon-06-light.png",
            },
            {
                "title": "Construction and Engineering Insurance",
                "content": "Insures construction projects against risks like property damage, liability, and delays.",
                "image": "/static/img/icon/icon-02-light.png",
            },
            {
                "title": "Marine Cargo and Hull Insurance",
                "content": "Protects goods transported by sea, as well as the vessels themselves.",
                "image": "/static/img/icon/icon-09-light.png",
            },
            {
                "title": "Credit and Financial Insurance",
                "content": "Covers losses resulting from non-payment by debtors.",
                "image": "/static/img/icon/icon-03-light.png",
            },
            {
                "title": "Oil and Energy Insurance",
                "content": "Insures risks associated with oil and gas exploration, production, and transportation.",
                "image": "/static/img/icon/icon-04-light.png",
            },
        ]
    },
    "appointment": {
        "title": "Zeal Insurance: Excellence in Service and Innovation",
        "content": "We are dedicated to exceeding client expectations through well-defined quality processes and providing time-bound, cost-effective solutions. Our holistic, interactive, versatile, and accurate approach ensures we deliver exceptional value and contribute to the industry's advancement.",
    },
    "team": {
        "title": "Meet Our Expert Team",
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
        "title": "Hear What Our Clients Say",
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


about_content = {
    "company_overview": {
        "headline": "About Zeal Insurance",
        "paragraph_1": "Zeal Insurance is a leading provider of innovative risk transfer and reinsurance solutions. We are committed to exceeding client expectations through unparalleled professionalism and dedication.",
        "feature1": "Licensing Membership",
        "feature2": "Management Expertise",
        "feature3": "Service Focus",
        "paragraph_2": "Zeal Insurance is licensed by the Insurance Regulatory and Development Authority (IRDA) and is a member of the Insurance Brokers Association of India.  Our team is comprised of seasoned professionals with strong connections to domestic and international insurance markets, ensuring our clients receive the most innovative risk transfer reinsurance solutions at the right price.",
    },
    "core_values": {
        "heading": "Our Core Values",
        "values": [
            "Professionalism",
            "Trust and mutual respect",
            "Commitment and responsive service",
            "Good corporate citizenship",
            "Ethics and Integrity",
            "Innovativeness and Entrepreneurship",
        ],
    },
    "mission_vision": {
        "heading": "Our Mission & Vision",
        "mission": "To be India's leading provider of risk, insurance, and reinsurance solutions globally, redefining professionalism and excellence.",
        "vision": "We identify client's needs and challenges to provide research-based solutions at competitive prices, while maximizing shareholder wealth through efficient resource utilization.",
    },
    "philosophy_approach": {
        "heading": "Our Philosophy & Approach",
        "philosophy": "Our business philosophy is to grow with the smaller accounts without discriminating in favor of our equally valued larger clients. No account is too big for us to handle promptly and efficiently, and nothing is too small or uneconomical for us to deal with once we have sought and accepted a client's portfolio of business. We believe that our business is both people focused and people orientated. We adhere to the highest standards of ethical and professional conduct.",
        "approach": "One of our most important assets is the relationships that we have with our clients. We are focused on building enduring relationships that are based on professionalism, transparency and competence. We believe that nurturing long-term relationships begins with listening to our clients, anticipating their needs, and working together with them to find the right solutions. It also means having a deep understanding of the risk environment and the markets in which our clients operate. We aim to assist our clients in the countries where they operate.",
    },
    "professional_role": {
        "heading": "Our Professional Role",
        "placement": "As an independent service provider, we negotiate the best insurance terms by fostering competition among insurers and reinsurers. This ensures our clients receive the most favorable coverage tailored to their needs.",
        "follow_up": "We provide comprehensive claims service and cost-effective, specialized insurance solutions, prioritizing our clients' best interests. Our commitment to excellence, professionalism, and innovation ensures top-tier customer service and industry contributions.",
    },
    "why_choose_us": {
        "heading": "Why Choose Zeal Insurance?",
        "reasons": [
            "We represent National / Multinational Insureds to Insurers, Direct Insurers to Reinsurers & Reinsurers to Retrocession Aires and alternative risk underwriters to risk bankers as we have good relationship in international market with insurers / syndicates / reinsurers / risk bankers with reliability and consistency",
            "We build bridges and break barriers through expertise between risk transferors and risk carriers and make availability of key decision makers and have ability to adapt to changes as per client needs.",
            "We share professional expertise and personalized “Know-How “in a business like approach & share up-to-date intelligence on global markets trends.",
            "We provide breadth and depth of underwriting knowledge and skills and specialist knowledge of offering effective and efficient solutions at competitive price.",
            "We combine report of a scientist, intuition of an artist and insight of a businessman and serve both sides like priest of marriage and not like an advocate of divorce.",
        ],
    },
}


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
        "about.html",
        about_content=about_content,
        global_content=global_content,
        enumerate=enumerate,
    )


@app.route("/service")
def service():
    return render_template(
        "service.html",
        global_content=global_content,
        service_content=home_content,
        enumerate=enumerate,
    )


@app.route("/admin/<page>")
def admin(page):
    return render_template("admin.html", page=page, home_content=home_content)


if __name__ == "__main__":
    app.run(debug=True)
