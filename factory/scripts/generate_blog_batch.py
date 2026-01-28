import os
import json
import sys

def load_config():
    """Load configuration from factory_config.json"""
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "factory_config.json"))
    if not os.path.exists(config_path):
        print(f"ERROR: Configuration file not found at {config_path}")
        sys.exit(1)
    
    with open(config_path, 'r') as f:
        return json.load(f)

config = load_config()
client = config.get("client", {})
brand = config.get("brand", {})

BUSINESS_NAME = client.get("name", "[BUSINESS_NAME]")
DOMAIN = client.get("domain", "[DOMAIN_NAME]")
PHONE = client.get("phone", "[PHONE_NUMBER]")
CLEAN_PHONE = "".join(filter(str.isdigit, PHONE))
PRIMARY_COLOR = brand.get("primary_color", "#0077be")

blog_template = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} | {BUSINESS_NAME} News</title>
    <meta name="description" content="{{description}}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://{DOMAIN}/blog/{{slug}}/">
    <meta property="og:title" content="{{title}}">
    <meta property="og:description" content="{{description}}">
    <meta property="og:image" content="/images/logo-og.png">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <link rel="stylesheet" href="/css/styles.css?v=1.0">
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
</head>

<body>

    <!-- Header -->
    <header>
        <div class="container">
            <a href="/" class="logo">{BUSINESS_NAME.split(' ')[0]} <span>{' '.join(BUSINESS_NAME.split(' ')[1:])}</span></a>
            <nav class="nav-menu">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/services/">Services</a></li>
                    <li><a href="/about/">About Us</a></li>
                    <li><a href="/blog/" class="active">Blog</a></li>
                    <li><a href="/contact/">Contact</a></li>
                </ul>
            </nav>
            <div class="header-actions">
                <a href="tel:{CLEAN_PHONE}" class="phone-link mobile-hide"><i class="fas fa-phone"></i> {PHONE}</a>
                <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
                <button class="mobile-menu-btn" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('/images/hero-bg.jpg'); padding: 80px 0; background-size: cover; background-position: center;">
        <div class="container" style="text-align: center;">
            <span style="color: #fff; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">{{category}}</span>
            <h1 style="color: white; font-size: 3rem; margin-top: 10px; max-width: 900px; margin-left: auto; margin-right: auto;">{{title}}</h1>
            <p style="color: rgba(255,255,255,0.9); margin-top: 15px;">Published by {BUSINESS_NAME}</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 60px 0; background: #fff;">
        <div class="container" style="max-width: 800px;">
            <div class="blog-content" style="line-height: 1.8; color: #444; font-size: 1.1rem;">
                <p class="lead" style="font-size: 1.3rem; color: {PRIMARY_COLOR}; font-weight: 600; margin-bottom: 30px;">
                    {{lead_text}}
                </p>
                
                {{content_body}}

                <div style="background: #f8f9fa; padding: 30px; border-left: 5px solid {PRIMARY_COLOR}; margin: 40px 0; border-radius: 4px;">
                    <h3 style="margin-top: 0; color: {PRIMARY_COLOR};">Ready to Get Started?</h3>
                    <p style="margin-bottom: 15px;">Contact us today for a free professional consultation.</p>
                    <a href="tel:{CLEAN_PHONE}" class="btn btn-primary">Call {PHONE}</a>
                </div>

                <hr style="margin: 50px 0; border: 0; border-top: 1px solid #eee;">
                
                <div style="font-size: 0.9rem; color: #666;">
                    <p><strong>Tags:</strong> {{tags}}</p>
                    <p><a href="/blog/">&larr; Back to All Articles</a></p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="aw-footer">
        <div class="container aw-footer-inner">
            <div class="aw-footer-brand" style="margin-bottom: 30px;">
                <h4 style="color: white;">{BUSINESS_NAME}</h4>
                <p style="opacity: 0.8; line-height: 1.6;">Your trusted professional service provider. Quality craftsmanship, reliable service.</p>
            </div>
            <div class="aw-footer-contact">
                <h4 style="color: white; margin-bottom: 15px;">Contact Us</h4>
                <p class="aw-footer-phone"><a href="tel:{CLEAN_PHONE}">{PHONE}</a></p>
            </div>
        </div>
        <div class="aw-footer-bottom">
            <p>© {BUSINESS_NAME}. All rights reserved. | <a href="/privacy/">Privacy Policy</a></p>
        </div>
    </footer>
    <script src="/js/script.js"></script>
</body>
</html>
"""

articles = [
    {
        "slug": "welcome-to-beauty-salon-av",
        "title": "Welcome to Beauty Salon: Antelope Valley's Premier Beauty Destination",
        "category": "Salon News",
        "description": "We are thrilled to unveil our new identity and expanded service menu for the Antelope Valley community.",
        "lead_text": "From expert color corrections to luxurious spa treatments, Beauty Salon is redefining self-care in Palmdale and Lancaster. Step inside our new digital home.",
        "tags": "Grand Opening, Hair, Skincare, Antelope Valley",
        "content_body": '''
            <h2>A New Era of Beauty</h2>
            <p>Welcome to <strong>Beauty Salon</strong>. Formerly known for our precise service and dedication, we have undergone a complete transformation to bring you a full-service beauty experience right here in the High Desert.</p>
            
            <h3>Expanded Services</h3>
            <p>We are no longer just about haircuts. Our new service menu includes:</p>
            <ul>
                <li><strong>Custom Color & Balayage:</strong> Our specialists use premium products to achieve vibrant, lasting results.</li>
                <li><strong>Spa-Grade Skincare:</strong> Rejuvenate your skin with our signature facials and chemical peels.</li>
                <li><strong>Beauty Bar:</strong> Lash lifts, brow lamination, and event makeup to get you ready for any occasion.</li>
            </ul>

            <h3>Why the Change?</h3>
            <p>We listened to our clients. You wanted a one-stop destination where trust and quality meet luxury. Our rebranded salon offers a serene atmosphere where you can relax and feel pampered.</p>

            <img src="/images/salon-hero-bg.jpg" alt="Beauty Salon Interior" style="width:100%; border-radius: 8px; margin: 20px 0;">

            <p>Explore our new site, check out our service pages, and book your appointment today. We can't wait to see you.</p>
        '''
    },
    {
        "slug": "hair-color-trends-2026",
        "title": "Top Hair Color Trends Taking Over 2026",
        "category": "Hair Trends",
        "description": "Discover the hottest hair colors of the year, from expensive brunettes to cowgirl copper.",
        "lead_text": "Thinking of a new look? This year is all about warmth, dimension, and healthy shine. Here are the top trends our stylists are loving.",
        "tags": "Hair Color, Balayage, 2026 Trends",
        "content_body": '''
            <h2>1. Expensive Brunette</h2>
            <p>Gone are the flat, dark colors. "Expensive Brunette" is all about rich, glossy depth. Think chocolate tones mixed with subtle caramel lowlights that catch the light perfectly.</p>

            <h2>2. Cowgirl Copper</h2>
            <p>Redheads are having a moment. This vibrant, warm copper shade is flattering on many skin tones and adds a bold statement to your look. It requires maintenance, but the results are stunning.</p>

            <img src="/images/hair-coloring.jpg" alt="Hair Coloring Service" style="width:100%; border-radius: 8px; margin: 20px 0;">

            <h2>3. Lived-In Blonde</h2>
            <p>High-maintenance roots are out. The lived-in blonde look uses a root smudge and seamless balayage to allow for a natural grow-out, meaning fewer trips to the salon without sacrificing that bright, sun-kissed vibe.</p>

            <h3>Maintain Your Color</h3>
            <p>No matter which trend you choose, home care is key. Ask our stylists about our color-safe shampoos and deep conditioning treatments to keep your new shade looking fresh.</p>
        '''
    },
    {
        "slug": "benefits-of-monthly-facials",
        "title": "Why Monthly Facials Are More Than Just a Treat",
        "category": "Skincare Advice",
        "description": "Understand the long-term benefits of professional facials for anti-aging and acne prevention.",
        "lead_text": "Skincare is a journey, not a destination. While a daily routine is crucial, professional treatments provide deep exfoliation and hydration that products alone can't match.",
        "tags": "Skincare, Facials, Anti-Aging, Wellness",
        "content_body": '''
            <h2>Deep Cleansing & Extraction</h2>
            <p>Even with great washing, pores can become clogged. Professional extractions remove buildup safely, preventing breakouts and refining pore size.</p>

            <h2>Increased Circulation</h2>
            <p>Facial massage isn't just relaxing—it boosts blood flow to the skin cells. This brings oxygen and nutrients to the surface, giving you that immediate "post-facial glow."</p>

            <img src="/images/skincare.jpg" alt="Relaxing Facial Treatment" style="width:100%; border-radius: 8px; margin: 20px 0;">

            <h2>Anti-Aging Benefits</h2>
            <p>Treatments involving exfoliation, microdermabrasion, or chemical peels stimulate cell turnover and collagen production. Over time, this reduces the appearance of fine lines and improves skin texture.</p>

            <h3>Book Your Glow</h3>
            <p>Ready to invest in your skin? Our licensed estheticians can create a customized plan for you. Schedule your consultation today.</p>
        '''
    }
]

def generate_articles():
    base_dir = "blog"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for article in articles:
        article_dir = os.path.join(base_dir, article['slug'])
        if not os.path.exists(article_dir):
            os.makedirs(article_dir)
            
        html_content = blog_template.format(
            title=article['title'],
            description=article['description'],
            slug=article['slug'],
            category=article['category'],
            lead_text=article['lead_text'],
            content_body=article['content_body'],
            tags=article['tags']
        )
        
        file_path = os.path.join(article_dir, "index.html")
        with open(file_path, "w") as f:
            f.write(html_content)
        
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    generate_articles()
