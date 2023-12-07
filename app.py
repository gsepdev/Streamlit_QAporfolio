 
import streamlit as st

from streamlit_option_menu import option_menu

from PIL import Image







with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Contact"],  #
        icons=["house", "book", "github","envelope"],  
        menu_icon="cast",
        default_index=0,
        #orientation="horizontal",

    )
#---------Home----------------------------
if selected == "Home":
    #st.title(f"show about me {selected}")
     # Mensaje de bienvenida
    st.markdown("## Welcome!")
    st.write("I am a passionate individual with expertise in software testing and quality assurance. Additionally, I am deeply interested in web development, with strong backend knowledge. My goal is to ensure the highest standards in product quality, leveraging my skills as a test analyst.")

    # Botones
    
   
    if st.button("About Me"):
       st.title("About Me")
        # Puedes agregar más contenido sobre ti aquí
       st.write("I am based in Melbourne and hold a Bachelor's degree in Business in Information Systems. I am a dynamic individual who thrives on challenges and strives to accomplish personal objectives.I am particularly drawn to the prospect of acquiring new skills and engaging with emerging technologies.With a strong foundation in Quality Assurance (QA), I bring expertise in ensuring the highest standards of product quality.")
        # Botón con el icono de GitHub


#-----end home-------------------------------------

#------Skills---------------------

if selected == "Skills":
    st.subheader(f"Technical {selected}")
    st.markdown("<style>div.stButton > button {margin-top: 800px;}</style>", unsafe_allow_html=True)
    #CERTIFICATIONS
    
  
    # Define la URL de la imagen 
    agile_image_url="https://bigr.io/wp-content/uploads/2021/04/agile-icon.png"
    github_image_url = "https://icones.pro/wp-content/uploads/2021/06/icone-github-rouge.png"
    sql_image_url = "https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg"
    azuredeveop_image_url="https://www.incredibuild.com/wp-content/uploads/2020/09/azure_devops-1.png"
    jira_image_url="https://1000logos.net/wp-content/uploads/2021/05/Atlassian-Logo-2010s1.png"
    python_image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png"
    #certification images 
    azure_funda_image_url="https://images.credly.com/images/be8fcaeb-c769-4858-b567-ffaaa73ce8cf/twitter_thumb_201604_image.png"
    azure_ai_image_url="https://images.credly.com/images/4136ced8-75d5-4afb-8677-40b6236e2672/azure-ai-fundamentals-600x600.png"
    scrum_master_image_url="https://www.scrumalliance.org/scrum/media/ScrumAllianceMedia/Files%20and%20PDFs/Certifications/CSM/SCR20146-Seals-Final-CSM.jpg"
    istqb_tester_image_url="https://istqb-backend-staging.s3.amazonaws.com/media/images/ISTQB_International_original_web.original.png"

    
       
    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.markdown(f'<img src="{agile_image_url}" width="120"></a>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<img src="{azuredeveop_image_url}" width="120"></a>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<img src="{jira_image_url}" width="120"></a>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<img src="{python_image_url}" width="70"></a>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<img src="{sql_image_url}" width="80"></a>', unsafe_allow_html=True)
    with col6:
        st.markdown(f'<img src="{github_image_url}" width="70"></a>', unsafe_allow_html=True)
    st.markdown("<style>div.stButton > button {margin-top: 900px;}</style>", unsafe_allow_html=True)
    st.subheader("Certifications")
    
    #CERTIFICATIONS
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        st.markdown(f'<img src="{azure_funda_image_url}" width="90"></a>', unsafe_allow_html=True)
        
    with col2:
        
        st.markdown(f'<img src="{azure_ai_image_url}" width="90"></a>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<img src="{scrum_master_image_url}" width="120"></a>', unsafe_allow_html=True)
        
    with col4:
        st.markdown(f'<img src="{istqb_tester_image_url}" width="140"></a>', unsafe_allow_html=True)



#------end skills--------------------------------------------


#----Projects-------------------------   

    
if selected == "Projects":
    st.title(f" QA   {selected}")
    img_project1_form=Image.open("images/QAportfolio.jpg")
    img_project2_form=Image.open("images/Testsuit.png")
    img_project3_form=Image.open("images/SeleniumIDE.png")
    img_project4_form=Image.open("images/Azure-devops.jpg")
    img_project5_form=Image.open("images/python.png")
  

    with st.container():
        st.write("---")
        st.header("##")
       
        image_column,text_column = st.columns((1, 2))
       
        with image_column:
           
             st.image(img_project1_form, width=200)
                  
            
        with text_column:
          
            st.subheader("QA Portfolio")
            st.write(
                """
                    Crafted using the Streamlit framework and implemented in Python,
                    my QA portfolio showcases a collection of meticulously designed projects 
                    that demonstrate my expertise in Quality Assurance.
                """
            )
            # Add some spacing between the image and text
            st.markdown("<style>div.stButton > button {margin-top: 200px;}</style>", unsafe_allow_html=True)
            
            github_url = "https://github.com/gsepdev/QAPortfolio"
            github_image_url = "https://icones.pro/wp-content/uploads/2021/06/icone-github-rouge.png"
            st.markdown(f'<a href="{github_url}" target="_blank"><img src="{github_image_url}" width="40"></a>', unsafe_allow_html=True)
    

    
    with st.container():
        st.write("---")        
        st.write("##")
        image_column,text_column = st.columns((1, 2))
        
        with image_column:
            st.image(img_project2_form,width=150)
           
        with text_column:
            st.subheader("Test Case Suite for QA Portfolio Website")
            st.write(
                """
                    This project focuses on the development of a comprehensive test case suite 
                    specifically tailored for the QA Portfolio Website. The goal is to ensure the robustness,
                    functionality, and security of the website, providing a thorough examination of its features 
                    and functionalities.
                """
            )
            github_url = "https://github.com/gsepdev/Testcases_QAportfolio"
            github_image_url = "https://icones.pro/wp-content/uploads/2021/06/icone-github-rouge.png"
            st.markdown(f'<a href="{github_url}" target="_blank"><img src="{github_image_url}" width="40"></a>', unsafe_allow_html=True)
            
    with st.container():
        st.write("---")
        st.write("##")
        image_column,text_column = st.columns((1, 2))
        with image_column:
            st.image(img_project3_form,width=130)
       

                        
        with text_column:
            st.subheader("Automatización de Pruebas de Portafolio QA con Selenium IDE")
            st.write(
                """
                This project focuses on test automation for the QA Portfolio using Selenium IDE.
                Automated tests with Selenium IDE will cover everything from basic navigation to validating 
                critical functions, providing a solid foundation for ongoing maintenance and evolution of 
                the QA Portfolio.

            
                """
            )
            

            github_url = "https://github.com/gsepdev/Selenium_QAportfolio"
            github_image_url = "https://icones.pro/wp-content/uploads/2021/06/icone-github-rouge.png"
            st.markdown(f'<a href="{github_url}" target="_blank"><img src="{github_image_url}" width="40"></a>', unsafe_allow_html=True)
                
          
    with st.container():
        st.write("---")
        st.write("##")
        image_column,text_column = st.columns((1, 2))
        with image_column:
           st.image(img_project4_form, width=150)
       
        
        with text_column:
            st.subheader("Scrum Portfolio Management with Azure DevOps")
            st.write(
                """
                    This project revolves around leveraging the power of Azure DevOps for agile portfolio 
                    management to enhance the planning, execution, and collaboration aspects of my QA Portfolio. 
                """
            )
            github_url = "https://github.com/gsepdev/AzureDeveop_QAPortfolio"
            github_image_url = "https://icones.pro/wp-content/uploads/2021/06/icone-github-rouge.png"
            st.markdown(f'<a href="{github_url}" target="_blank"><img src="{github_image_url}" width="40"></a>', unsafe_allow_html=True)
    with st.container():
        st.write("---")        
        st.write("##")
        image_column,text_column = st.columns((1, 2))
        with image_column:
            st.image(img_project5_form,width=100)
                        
           
        with text_column:
            st.subheader("Pythonic GUI Adventures")
            st.write(
                """
                The "Pythonic GUI Adventures" project focuses on developing entry-level exercises using 
                the Python programming language and the Tkinter library for graphical user interfaces (GUI). 
                """
            )
            github_url = "https://github.com/gsepdev/python"
            github_image_url = "https://icones.pro/wp-content/uploads/2021/06/icone-github-rouge.png"
            st.markdown(f'<a href="{github_url}" target="_blank"><img src="{github_image_url}" width="40"></a>', unsafe_allow_html=True)
        
#------end projects------------------------------------------
      
  #---------Contact---------------------     


if selected == "Contact":
    st.title(f" {selected}")
    st.write("Feel free to contact me through the following platforms:")
   
              
        # Define la URL de GitHub/linkedin
    github_url = "http://github.com/gsepdev"
    github_url2 = "http://linkedin.com"
    # Define la URL de la imagen de GitHub
    github_image_url = "https://icones.pro/wp-content/uploads/2021/06/icone-github-rouge.png"
    github_image_url2 = "https://i.pinimg.com/736x/96/8e/a6/968ea62882943e88bbd318ae5fa67429.jpg"

    col1, col2 = st.columns(2)
    # Muestra la imagen con un enlace en HTML( hiperlink)
    with col1:
        st.markdown(f'<a href="{github_url}" target="_blank"><img src="{github_image_url}" width="50"></a>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<a href="{github_url2}" target="_blank"><img src="{github_image_url2}" width="60"></a>', unsafe_allow_html=True)

 
    
   


    



        

