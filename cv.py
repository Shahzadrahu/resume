import streamlit as st

def generate_cv(name, email, phone, education, experience, skills):
    cv = f"""
    # Curriculum Vitae
    
    ## Personal Information
    - **Name:** {name}
    - **Email:** {email}
    - **Phone:** {phone}
    
    ## Education
    - {education}
    
    ## Experience
    - {experience}
    
    ## Skills
    - {skills}
    """
    return cv

def main():
    st.title("CV Generator")

    # Get user input
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    education = st.text_area("Education", "Degree, University, Year")

    experience = st.text_area("Experience", "Job Title, Company, Year")

    skills = st.text_area("Skills", "Skill 1, Skill 2, Skill 3")

    if st.button("Generate CV"):
        # Generate and display the CV
        cv = generate_cv(name, email, phone, education, experience, skills)
        st.markdown(cv, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
