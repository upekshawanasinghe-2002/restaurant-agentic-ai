import streamlit as st
import sys
import os
import time


# ============================================================
# Import Agents
# ============================================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from agents.router_agent import RouterAgent


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="AI Restaurant Planner",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# Premium CSS
# ============================================================

st.markdown(
"""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap'
);


html, body, [class*="css"] {

    font-family:'Poppins', sans-serif;

}


/* Background */

.stApp {

    background:
    linear-gradient(
        135deg,
        #f8fbff,
        #eaf3ff
    );

}



/* Hide Streamlit */

#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

header {
    visibility:hidden;
}



/* Hero */

.hero {

    background:
    linear-gradient(
        135deg,
        #0f172a,
        #2563eb
    );

    padding:50px;

    border-radius:30px;

    color:white;

    box-shadow:
    0 20px 50px rgba(0,0,0,0.25);

    margin-bottom:35px;

}


.hero h1 {

    font-size:48px;

    font-weight:800;

}


.hero p {

    font-size:20px;

    opacity:0.9;

}



/* Cards */


.card {

    background:white;

    padding:30px;

    border-radius:25px;

    box-shadow:
    0 15px 35px rgba(0,0,0,0.08);

}



/* Result */

.result {

    background:white;

    padding:30px;

    margin-top:30px;

    border-radius:25px;

    border-left:
    8px solid #2563eb;

    box-shadow:
    0 15px 40px rgba(0,0,0,0.1);

}



/* Buttons */

.stButton > button {


    width:100%;

    height:60px;

    border-radius:15px;

    border:none;

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    );

    color:white;

    font-size:18px;

    font-weight:700;


}


.stButton > button:hover {

    transform:scale(1.02);

}



/* Inputs */


.stTextInput input {

    border-radius:15px;

}


</style>

""",
unsafe_allow_html=True
)



# ============================================================
# Hero Section
# ============================================================


st.markdown(
"""

<div class="hero">

<h1>
🍽️ AI Restaurant Recommendation & Dining Planner
</h1>


<p>

Discover Sri Lanka's best restaurants using
Agentic AI + Retrieval Augmented Generation.

</p>


</div>

""",
unsafe_allow_html=True
)



# ============================================================
# Main Layout
# ============================================================


left, right = st.columns(
    [2,1],
    gap="large"
)



# ============================================================
# Search Card
# ============================================================


with left:


    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )


    st.markdown(
        "## 🍴 Plan Your Perfect Dining Experience"
    )


    st.write(
        """
Tell our AI what you need and get a
personalized restaurant recommendation.
"""
    )



    food = st.text_input(
        "🍜 Preferred Cuisine",
        placeholder=
        "Seafood, Kottu, Vegetarian, Italian..."
    )



    location = st.text_input(
        "📍 Destination",
        placeholder=
        "Colombo, Galle, Kandy..."
    )



    budget = st.slider(
        "💰 Budget (LKR)",
        1000,
        200000,
        6000,
        500
    )



    st.markdown(
        "### ⭐ Popular Choices"
    )


    c1,c2,c3,c4 = st.columns(4)


    with c1:
        st.info("🐟 Seafood")


    with c2:
        st.info("🥗 Vegetarian")


    with c3:
        st.info("🍛 Sri Lankan")


    with c4:
        st.info("🍕 Italian")



    search = st.button(
        "🔍 Find My Perfect Restaurant"
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )





# ============================================================
# Feature Card
# ============================================================


with right:


    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )


    st.markdown(
        "## 🤖 Why Choose AI?"
    )


    features = [

        "🤖 Multi-Agent AI",

        "📚 RAG Knowledge Base",

        "⭐ Personalized Suggestions",

        "⚡ Groq Fast LLM",

        "💰 Budget Awareness",

        "📍 Location Intelligence"

    ]


    for item in features:

        st.success(item)



    st.markdown("---")


    st.markdown(
        """
### 🇱🇰 Explore Sri Lanka

✔ Hidden restaurants

✔ Local cuisine

✔ Fine dining

✔ Travel plans

✔ AI recommendations

"""
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )





# ============================================================
# AI Result Section
# ============================================================


if search:


    if food == "" or location == "":

        st.warning(
            "Please enter cuisine and destination."
        )


    else:


        user_input = (

            f"Find {food} restaurants "

            f"in {location} "

            f"under {budget} LKR"

        )



        router = RouterAgent()



        with st.spinner(
            "🤖 AI Agents are analysing restaurants..."
        ):


            result = router.run(
                user_input
            )

            time.sleep(1)



        st.markdown(
        """

        <div class="result">

        <h2>
        🍽️ Your Personalized Dining Plan
        </h2>

        </div>

        """,
        unsafe_allow_html=True
        )


        st.success(
            "✅ Dining plan generated successfully!"
        )


        st.write(result)




# ============================================================
# Statistics
# ============================================================


st.markdown("---")


col1,col2,col3 = st.columns(3)


with col1:

    st.metric(
        "🤖 AI Agents",
        "4+"
    )


with col2:

    st.metric(
        "📚 Knowledge Base",
        "RAG"
    )


with col3:

    st.metric(
        "⚡ LLM Engine",
        "Groq"
    )



# ============================================================
# Footer
# ============================================================


st.markdown("---")


st.markdown(
"""

<div style="
text-align:center;
color:#64748b;
font-size:15px;
">


🌴 <b>
AI Restaurant Recommendation & Dining Planner
</b>


<br><br>


Powered by

<b>
Agentic AI • LangChain • ChromaDB • Groq • Streamlit
</b>


<br><br>


© 2026 All Rights Reserved


</div>


""",
unsafe_allow_html=True
)