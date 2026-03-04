def build_prompt(destination, days, budget, style, interests, start_city, traveler_type):

    # -----------------------
    # Travel Style Rules
    # -----------------------
    style_rules = ""

    if style == "Relaxed":
        style_rules = """
Travel Style Guidelines:
- Limit to 2 major activities per day
- Add slow mornings and free time
- Include relaxation time (cafes, beaches, parks)
- Avoid long travel distances in one day
- Keep schedule flexible and easy
"""

    elif style == "Balanced":
        style_rules = """
Travel Style Guidelines:
- Include 3–4 well-grouped activities per day
- Mix sightseeing with relaxation
- Keep travel time practical
"""

    elif style == "Packed":
        style_rules = """
Travel Style Guidelines:
- Include 4–6 activities per day
- Maximize sightseeing coverage
- Optimize routes to reduce time waste
- Minimize idle/free time
- Use early starts and efficient planning
"""

    # -----------------------
    # Traveler Type Rules
    # -----------------------
    traveler_rules = ""

    if traveler_type == "Solo":
        traveler_rules = """
Traveler Type Guidelines:
- Focus on flexibility
- Suggest hostels or budget rooms
- Add solo-friendly cafes and safe areas
"""

    elif traveler_type == "Couple":
        traveler_rules = """
Traveler Type Guidelines:
- Include romantic spots and sunset locations
- Suggest private rooms or boutique stays
- Add cozy cafes and scenic dinners
- Include peaceful and scenic experiences
"""

    elif traveler_type == "Friends":
        traveler_rules = """
Traveler Type Guidelines:
- Include fun group activities
- Add nightlife or social spots
- Suggest group stays or hostels
- Include adventure or shared experiences
"""

    elif traveler_type == "Family":
        traveler_rules = """
Traveler Type Guidelines:
- Include child-friendly attractions
- Avoid late-night activities
- Suggest comfortable hotels
- Keep travel distances minimal
- Prioritize safety and convenience
"""

    # -----------------------
    # Budget Rules
    # -----------------------
    budget_rules = ""

    if budget == "Low":
        budget_rules = """
Budget Guidelines:
- Suggest hostels, guesthouses, or budget hotels
- Prefer public transport or scooter rentals
- Focus on affordable eateries and local food
- Keep daily cost between ₹1000–2500 per person
"""

    elif budget == "Medium":
        budget_rules = """
Budget Guidelines:
- Suggest 3-star hotels or boutique stays
- Use cabs or rental vehicles when practical
- Mix casual and premium dining
- Keep daily cost between ₹3500–8000 per person
"""

    elif budget == "Luxury":
        budget_rules = """
Budget Guidelines:
- Suggest 4–5 star hotels or premium resorts
- Recommend private transport or chauffeur services
- Include fine dining experiences
- Keep daily cost above ₹12000 per person
"""

    # -----------------------
    # Final Prompt
    # -----------------------
    return f"""
You are an expert professional travel planner.

Create a highly detailed and structured {days}-day travel itinerary for {destination}.

Traveler Profile:
- Budget: {budget}
- Travel Style: {style}
- Interests: {interests}
- Starting City: {start_city}
- Traveling As: {traveler_type}

{style_rules}

{traveler_rules}

{budget_rules}

STRICT FORMAT:

Start with:
==============================
TRIP OVERVIEW
==============================

Then:

==============================
DAY 1
==============================
Morning:
Afternoon:
Evening:
Estimated Daily Cost:

Repeat for all {days} days.

Then:

==============================
FOOD RECOMMENDATIONS
==============================

==============================
HIDDEN GEMS
==============================

==============================
INSTAGRAM SPOTS
==============================

==============================
TOTAL ESTIMATED BUDGET
==============================

Rules:
- Group nearby attractions
- Avoid unrealistic schedules
- Keep travel time practical
- Include accommodation cost
- Budget must align with realistic Indian ranges
- Keep response clean and structured
"""