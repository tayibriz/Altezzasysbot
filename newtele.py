import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler , ConversationHandler
from telegram.ext.filters import Filters 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
import mysql.connector
import re



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define your bot token
TOKEN = "6311385456:AAEfWRzJNici2DkNWX1VgxgcW8BkcpcOjCM"

#settingupdatabase
db_config = {
    'user': 'root',
    'password': 'QAZ!@2023',
    'host': 'db',
    'database': 'mybot',
}

def create_database():
    conn = mysql.connector.connect(**db_config)
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mybot")
        cursor.close()
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

def create_users_table():
    conn = mysql.connector.connect(**db_config)
    try:
        cursor = conn.cursor()
        cursor.execute("USE mybot")
        cursor.execute("CREATE TABLE IF NOT EXISTS users ("
                       "user_id BIGINT AUTO_INCREMENT PRIMARY KEY, "
                       "country VARCHAR(255), "
                       "email VARCHAR(255), "
                       "contact VARCHAR(20))"
                       )
        cursor.close()
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()




AWAITING_COUNTRY,AWAITING_EMAIL, AWAITING_CONTACT = range(3)

# Command handler for /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Welcome to the Altezzasys Services ChatBot.
Empowering the space of cutting edge technologies with our Services of
1. /Blockchain 
2. /AI_ML 
3. /Web_Dev 
4. /Mobile_Apps 
5. /Talent_acquisition
                             
                             
                             
                             ''')
    
    

def handle_message(update,context):
    update.message.reply_text(f' you said :{update.message.text}')

#markdown for blockchain
def Blockchain(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Blockchain is a technology that enables secure and transparent digital transactions without the need for intermediaries. It was originally developed for the cryptocurrency Bitcoin, but it has since been applied to many other industries and use cases. One of the main benefits of blockchain is its decentralization, which means that no single entity controls the network or the data stored on it. Instead, the network is maintained and updated by a community of users, making it more transparent.
Services of Blockchain provided by Us are:
1. /Metaverse_Development
2. /Uniswap_Clone_Development
3. /Smart_Contracts_Development
4. /Smart_Contracts_Audit
5. /Blockchain_DApps 
6. /Dex_Development 
7. /DAO_Development
8. /DeFi_Development
9. /ICO_Launchpads
10. /IDO_Launchpads
11. /Centralized_Exchange
12. /Cryptocurrency_Development
13. /NFT_Marketplace_Development
14. /Pancakeswap_Clone_Development
15. /Crypto_Bots_Develop


''')
    


#markdownof blockchain
def Metaverse_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Metaverse development is revolutionizing online interaction by enabling users to transcend the boundaries of traditional web browsing. It fosters a fully immersive and interconnected digital realm where people can engage with computer-generated environments and each other in real time. With the metaverse, the internet is evolving into a dynamic, multi-dimensional space that merges physical and virtual realities. It holds the promise of unlocking endless possibilities for entertainment, communication, commerce, education, and more, offering a new paradigm for human interaction and expression.

''')
    button(update, context)

def Uniswap_Clone_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Uniswap is a decentralized cryptocurrency exchange built on the Ethereum blockchain. It operates on the concept of automated liquidity provision, allowing users to trade various ERC-20 tokens directly from their Ethereum wallets. Uniswap utilizes smart contracts and liquidity pools, where users can provide liquidity by depositing their tokens into the pool and earning fees in return. The platform offers a seamless and decentralized trading experience.
''')
    button(update, context)
                             


def Smart_Contracts_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Smart contracts, leveraging the power of blockchain technology, have revolutionized transactional processes by eliminating intermediaries and enabling decentralized business operations. However, the intricate nature of smart contracts necessitates meticulous scrutiny and expert evaluation to mitigate potential security risks, bugs, financial losses, and reputational damage, ensuring robust and trustworthy implementation.
''')
    button(update, context)
                             


def Smart_Contracts_Audit(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Smart contract audits are crucial to ensure the integrity and security of blockchain applications. By conducting a smart contract audit, potential vulnerabilities and weaknesses in the code can be identified and addressed, reducing the risk of hacking, exploits, and financial losses. It helps ensure that the smart contract functions as intended, mitigates the possibility of unforeseen bugs or errors, and enhances the overall reliability and trustworthiness of the blockchain system. Smart contract audits provide an added layer of confidence for users, developers, and stakeholders in the security and proper functioning of the decentralized application.
''')
    button(update, context)
                             


def Blockchain_DApps(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Altezzasys offers seamless integration and user-friendly UX design as part of our comprehensive dApp development solutions. Our dedicated team of blockchain developers, full-stack developers, and UX designers deploy their expertise to deliver end-to-end solutions. We cater to various industries and startups, including healthcare, supply chain and logistics, utility, and more. Our skilled dApp developers excel at transforming ideas into powerful applications that propel your business to new heights. Leveraging the potential of decentralized applications or dApps, we enable interactions with smart contracts (e.g., tokens) on a peer-to-peer network of servers. These open-source applications are developed on diverse blockchain platforms like Ethereum, EOS, Hyperledger, Polkadot, and others.
''')
    button(update, context)
                             


def Dex_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''In the world of decentralized finance (DeFi), several important concepts and platforms exist. Automated Market Makers (AMMs) play a crucial role in facilitating trading, while hybrid/alternative platforms offer innovative solutions. Order books can be implemented on-chain or off-chain, providing flexibility in trade execution. Multi-level marketing (MLM) strategies may also be utilized in certain contexts. Ethereum DEX and BSC DEX refer to decentralized exchanges built on the Ethereum and Binance Smart Chain networks, respectively. DEX with AMM denotes decentralized exchanges that incorporate automated market maker functionality. Lastly, the 0X Protocol is a notable framework for enabling peer-to-peer trading on the blockchain.
''')
    button(update, context)
                             


def DAO_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''The DAO (Decentralized Autonomous Organization) represents a unique type of organizational structure operated by computer code and explicit rules. It functions as an investment fund that assists start-ups in realizing their projects. What sets it apart from conventional organizations is its utilization of smart contracts on the blockchain. These smart contracts facilitate and enforce the interactions and transactions between the DAO, investors, and fund managers, ensuring a high level of transparency throughout the process. This decentralized and automated approach offers new opportunities for collaboration, decision-making, and resource allocation within the realm of investment and entrepreneurship.
''')
    button(update, context)
                             


def DeFi_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''We specialize in offering DeFi platform development services, empowering businesses to leverage the transformative potential of decentralized finance. Our team of experts combines their in-depth knowledge of blockchain technology, smart contract development, and financial systems to create robust and secure DeFi platforms. With our services, clients can unlock a wide range of decentralized financial solutions, including lending and borrowing protocols, decentralized exchanges (DEXs), yield farming platforms, asset management systems, and more. We understand the importance of security, scalability, and user experience in DeFi applications, and we strive to deliver customized solutions that meet our clients' specific requirements. By embracing DeFi, businesses can tap into a global and permissionless financial ecosystem, offering users greater financial inclusivity, transparency, and control over their assets.
''')
    button(update, context)
                             


def ICO_Launchpads(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Our team of experienced domain experts specializes in ICO development services, enabling you to maximize fundraising opportunities for your project. As early adopters of ICOs, we provide comprehensive assistance in launching your own ICO, ensuring the design of a secure protocol that safeguards your ETH, BTC, and other cryptocurrencies. Partner with Mobiloitte, the leading ICO launch company, to bring your vision to life and achieve fundraising success.
''')
    button(update, context)
                             


def IDO_Launchpads(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''IDO Token Launchpad serves as a trusted platform for emerging crypto projects to raise funds through a transparent and credible process. It brings together prospective investors and project creators, providing a fair and efficient fundraising mechanism. Through multi-tiered staking protocols, investors can participate in various funding rounds of the projects, allowing for wider participation and potential investment opportunities.Initial DEX Offering launchpad is a pre-made software that is used to setup and run a custom decentralized token marketplace. A decentralized token marketplace assists the investors to discover the latest upcoming cryptocurrency projects and fund those projects by buying them at a special pre-sale.
''')
    button(update, context)
                             


def Centralized_Exchange(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''A cryptocurrency exchange is a digital platform that enables individuals to buy, sell, and trade cryptocurrencies, such as Bitcoin, Ethereum, and others. It serves as an intermediary that matches buyers with sellers, facilitating transactions within the cryptocurrency market. These exchanges often provide various trading features, including order types, price charts, and liquidity pools, offering users a range of options to participate in the crypto market. Additionally, some exchanges may offer additional services like wallet storage and fiat currency integration to enhance user experience and accessibility.
''')
    button(update, context)
                             


def Cryptocurrency_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Unlock the potential of cryptocurrency with our cutting-edge software platforms developed by our innovative cryptocurrency development company. Whether you seek altcoin development or cryptocurrency wallet services, we have you covered. A cryptocurrency wallet acts as a secure software program, enabling users to store private and public keys, conduct transactions, and monitor their digital currency balance across multiple blockchains. Embrace the world of Bitcoin and other cryptocurrencies by securing your own digital wallet today.
''')
    button(update, context)
                             


def NFT_Marketplace_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Our team specializes in building NFT marketplaces that cater to diverse industries, empowering artists, brands, and gaming platforms to showcase unique digital assets and engage a global audience. Whether you're an artist seeking to monetize creations, a brand aiming to connect with customers through digital collectibles, or a gaming platform looking to enhance user experiences with NFT integration, our experts have the knowledge and flexibility to bring your vision to life. We tailor our NFT marketplace solutions to your specific needs, leveraging our understanding of industry intricacies for optimal results.
''')
    button(update, context)
                             


def Pancakeswap_Clone_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Pancakeswap is a decentralized cryptocurrency exchange built on the BSC blockchain. It operates on the concept of automated liquidity provision, allowing users to trade various ERC-20 tokens directly from their Ethereum wallets. Pancakeswap utilizes smart contracts and liquidity pools, where users can provide liquidity by depositing their tokens into the pool and earning fees in return. The platform offers a seamless and decentralized trading experience, with no need for intermediaries or traditional order books. Pancakeswap has gained significant popularity within the decentralized finance (DeFi) ecosystem and has played a pivotal role in enabling users to easily swap and trade tokens while promoting liquidity and transparency in the cryptocurrency market.
''')
    button(update, context)
                             


def Crypto_Bots_Develop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Altezzasys, a renowned company in Crypto Trading Bot development, provides exceptional services for creating advanced trading bots for crypto projects, investment platforms, and both centralized and decentralized environments. With our expert team of developers, we tailor the development process to meet clients' specific business requirements, leveraging cutting-edge technology and robust security practices to deliver high-performance bots that facilitate profitable trading and attract a large user base.
''')
    button(update, context)



#methods of ai ml
def AI_ML(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''AI/ML technologies are transforming industries across the board, and their impact on various sectors is profound. In healthcare, AI/ML is revolutionizing medical diagnostics, drug discovery, and patient care, leading to improved outcomes and personalized treatments. In finance, these technologies are automating risk assessment, fraud detection, and trading strategies, enhancing efficiency and security in financial operations. In manufacturing, AI/ML is optimizing production processes, enabling predictive maintenance.
Altezzasys provides these services in AI & Ml tech:
1./Generative_AI_Services 
2./AI_Consulting
3./Data_Science_Consulting 
4./Machine_Learning 
5./Computer_Vision
6./Natural_Language_Processing
7./Robotics_Process_Automation
8./Predictive_Analysis
''')
    


def Generative_AI_Services(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Generative AI has the potential to bring about significant changes in various aspects of the world. In creative industries, it can revolutionize art, music, and design by assisting artists in generating innovative content. Content generation can be automated, benefiting journalists and marketers with personalized and relevant material. Gaming and virtual reality experiences can become more immersive with generative AI, creating realistic virtual worlds. Personalized healthcare can be achieved through AI's analysis of vast medical data. Humanitarian efforts can be supported through AI-generated models for disaster response planning and resource allocation.
''')
    button(update, context)



def AI_Consulting(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''The influence of AI on technology stems from its impact on computing capabilities. AI empowers computers to process vast volumes of data and leverage their acquired intelligence to make optimal decisions and discoveries in a fraction of the time it would take humans. AI has made significant strides since its inception in 1951 when Christopher Strachey achieved a breakthrough by developing an AI computer program that successfully played a game of checkers on the Ferranti Mark I computer at the University of Manchester. Since then, AI has been instrumental in diverse fields such as sequencing RNA for vaccines and modeling human speech. These applications rely on machine learning algorithms and models, with a growing emphasis on perception, reasoning, and generalization.
''')
    button(update, context)



def Data_Science_Consulting(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''The future of data science consulting is poised for remarkable growth and evolution as organizations increasingly recognize the value of data-driven decision-making. With the exponential growth of data, emerging technologies, and the increasing demand for actionable insights, data science consulting will play a pivotal role in helping businesses unlock the full potential of their data. Consultants will focus on advanced analytics, machine learning, and artificial intelligence techniques to extract valuable insights from vast and complex datasets.
''')
    button(update, context)



def Machine_Learning(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''In the future, machine learning is poised to become even more ubiquitous and seamlessly integrated into our daily lives. As the volume of data continues to grow exponentially, machine learning algorithms will become increasingly sophisticated in their ability to extract meaningful insights and patterns. This will lead to more accurate predictions, enhanced automation, and improved decision-making across a wide range of applications. Machine learning will also contribute to the development of innovative technologies like self-driving cars, intelligent virtual assistants, and personalized medicine. With ongoing advancements in deep learning, natural language processing, and reinforcement learning, the future of machine learning holds the promise of transforming industries, optimizing processes, and empowering individuals and organizations to unlock the full potential of data-driven intelligence.
''')
    button(update, context)



def Computer_Vision(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Integrate computer vision services seamlessly with existing systems like ERP, POS, CCTV, and diagnostic software to create innovative applications. Our solutions detect anomalies in production lines, analyze medical images, and identify products and individuals on social media, among other possibilities. Additionally, our expertise in machine learning integration enables the development of diverse enterprise applications and cloud services. Our team has designed cutting-edge artificial intelligence and computer vision-based applications with advanced components including object classification, feature recognition, segmentation, pattern recognition, object detection, and filtering. We can assist you in building prototypes that require minimal resources and without the need for additional hardware support, meeting the unique requirements of various industries.
''')
    button(update, context)



def Natural_Language_Processing(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''we provide cutting-edge natural language processing services that combine artificial intelligence, machine learning, and linguistics. Our team of experts specializes in integrating NLP capabilities into applications, bots, and IoT devices, enabling you to streamline complex processes and rapidly process documents. With our NLP expertise, your enterprise can develop a next-generation digital assistant that is contextually aware, comprehends natural language, and makes informed decisions. Partnering with us empowers your organization to unlock the full potential of NLP and harness its benefits for improved efficiency and decision-making.
''')
    button(update, context)


def Robotics_Process_Automation(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Implementing Robotic Process Automation (RPA) offers numerous benefits to organizations across various industries. Firstly, RPA enables significant time and cost savings by automating repetitive and rule-based tasks, freeing up human resources to focus on more strategic and value-added activities. Additionally, RPA enhances operational efficiency by reducing errors and improving process accuracy. It ensures 24/7 availability and consistency in task execution, leading to improved productivity and customer satisfaction. Moreover, RPA facilitates process standardization and compliance, ensuring adherence to regulations and reducing the risk of non-compliance. Overall, the adoption of RPA streamlines operations, drives efficiency, and empowers organizations to achieve higher productivity and competitive advantage in the dynamic business landscape.
''')
    button(update, context)


def Predictive_Analysis(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Predictive analytics, a branch of data science, leverages machine learning algorithms and historical data to forecast future events. This versatile technology finds applications across industries, enabling trend identification, demand prediction, and informed decision-making for pricing and marketing strategies. At Altezzasys, we excel in crafting tailor-made predictive analytics solutions that empower our clients to harness the potential of their data. With our team of skilled data scientists and machine learning engineers, we collaborate closely with you to comprehend your precise objectives and develop a customized solution that aligns with your specific requirements.
''')
    button(update, context)


#webdev markup
def Web_Dev(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''We are one the Premium agency to help you shape your vision for any kind of web development.
Altezzasys provides these services in Web development:
1./Website_Development
2./Web_Apps_Development 
3./SAAS_Development 
4./Shopify_Development
5./WordPress_Deveopment 
6./MEAN_MERN_Stack
''')
    
def Website_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Our team utilizes cutting-edge technologies, including MEAN Stack, MERN Stack, PHP, Python Web 2.0, Shopify, WordPress, Drupal, Magento, and .Net to develop responsive and customized web applications for your business. With extensive experience, we harness the dynamic nature of opensource technologies combine it with database languages like MySQL, HTML, CSS, JavaScript. As a leading web app development company, we have established ourselves as experts in leveraging the latest web technologies to address diverse project requirements. We go beyond technical aspects and dedicate ourselves to the marketing aspects as well. By maintaining open and effective communication and following the Agile approach, we consistently deliver exceptional results within estimated timeframes.
''')
    button(update, context)



def Web_Apps_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''As a highly sought-after provider of custom software development services, we thoroughly analyze your business requirements, conceptualize software solutions, and ensure that you derive maximum value from its development. Our expert team further aids you in selecting the optimal technology stack by carefully reviewing the advantages and disadvantages of various technologies before commencing the project.
''')
    button(update, context)



def SAAS_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''At our company, we are committed to building durable SaaS products that not only support your growth but also enhance your customers' experience. Our team of experts is dedicated to designing and developing Software-as-a-Service solutions tailored to meet your specific needs. By leveraging our expertise, we aim to transform the way your customers interact with your products or services, resulting in a seamless and satisfying experience. With our focus on longevity and customer satisfaction, our SaaS products are built to stand the test of time and contribute to your business growth.
''')
    button(update, context)



def Shopify_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Altezzasys is a renowned Shopify development company known for its exceptional eCommerce development services catering to a wide range of industries. With our profound expertise in Shopify store development, we create compelling solutions that boast top-of-the-line features and functionalities. When you choose Altezzasys for your eCommerce website development or Shopify store development, you benefit from our team of highly skilled professionals who leverage the full potential of the Shopify platform. We pride ourselves on delivering customized solutions that align with your unique business requirements and reflect your brand identity. Our focus on integrating best-in-class features, seamless third-party integrations, timely project delivery, and reliable ongoing support sets us apart. Trust Altezzasys to empower your online business and drive success in the dynamic world of eCommerce.
''')
    button(update, context)



def WordPress_Deveopment(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''As a leading web development company, we specialize in delivering end-to-end digital solutions, encompassing the entire process from conceptualization to deployment. Our expertise extends to data migration, API integrations, and plugin development, ensuring seamless functionality and enhanced performance. We are particularly skilled in developing high-performing WordPress websites that not only captivate users but also drive better business outcomes. Our WordPress websites are designed to be user-friendly, easily manageable, and optimized for success.
''')
    button(update, context)



def MEAN_MERN_Stack(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''To ensure speed, efficiency, and scalability, MEAN Stack is an excellent choice. It is a JavaScript technology platform that enables the development of robust, flexible, and feature-rich applications. It comprises four cutting-edge JavaScript-based technologies: MongoDB, Express.js, Angular.js, and Node.js. MEAN Stack is commonly utilized for both front-end and back-end development, making it a versatile solution for building web applications. On the other hand, MERN Stack is similar to MEAN Stack, with the "R" representing ReactJS instead of Angular.js. MERN Stack is highly favored by companies aiming to create high-quality web applications.
''')
    button(update, context)



#Mobile_Apps
def Mobile_Apps(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''We develop Next-Gen Mobile Apps that are approved as per industry standards with future forward mobile app development services.
Altezzasys provides these services in Mobile App development:
1./Native_IOS_Apps_Development 
2./ARVR_Apps
3./Progressive_Web_Apps_Development 
4./Flutter_Apps_Development 
5./React_Native_Apps_Development 
6./Native_Android_Apps_Development
''')
    

def Native_IOS_Apps_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''At our core, we are not confined to smartphones alone. Our prowess in iOS mobile app development transcends boundaries, showcasing our mastery across an array of iOS devices and platforms. Embracing the full spectrum of possibilities, we have delved deep into the iOS realm, leaving no stone unturned. From smartphones to tablets, from iOS Wear to Ios TV, we fearlessly explore every avenue. Armed with a battle-tested tech stack, our ingenious iOS app developers craft apps that mesmerize users and surpass the million-download mark on the prestigious Google Play Store.
''')
    button(update, context)



def ARVR_Apps(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''AltezzaSys is a leading AR VR development company that helps startups and establishments employ the raw power of augmented and virtual reality to enthrall users and multiply your ROI.With consumer expectations constantly on the rise, individuals are seeking innovative methods to engage with businesses and maximize the value they receive. Our primary objective is to assist businesses in meeting these expectations by offering new and inventive ways of interaction.Our team excels in AR/VR development and is renowned for introducing agile, user-centric, and measurable product development practices.
''')
    button(update, context)



def Progressive_Web_Apps_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''By leveraging progressive web app development, we specialize in constructing state-of-the-art web applications that offer a fully immersive experience akin to desktop or mobile apps. Our team of experts is dedicated to creating captivating digital experiences that go beyond traditional websites. We combine cutting-edge technologies, responsive design, and intuitive interfaces to provide users with a seamless and engaging journey. At the core of our approach is optimizing user engagement. We understand that capturing and retaining users' attention is crucial for the success of your business.
''')
    button(update, context)



def Flutter_Apps_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''At our core, we are not confined to smartphones alone. Our prowess in Flutter mobile app development transcends boundaries, showcasing our mastery across an array of android devices and platforms. Embracing the full spectrum of possibilities, we have delved deep into the Flutter realm, leaving no stone unturned. From smartphones to tablets, from iOS Wear to Ios TV, we fearlessly explore every avenue. Armed with a battle-tested tech stack, our ingenious Flutter app developers craft apps that mesmerize users and surpass the million-download mark on the prestigious Google Play Store.
''')
    button(update, context)



def React_Native_Apps_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''At our core, we are not confined to smartphones alone. Our prowess in ReactNative mobile app development transcends boundaries, showcasing our mastery across an array of React devices and platforms. Embracing the full spectrum of possibilities, we have delved deep into the React realm, leaving no stone unturned. From smartphones to tablets, from iOS Wear to Ios TV, we fearlessly explore every avenue. Armed with a battle-tested tech stack, our ingenious iOS app developers craft apps that mesmerize users and surpass the million-download mark on the prestigious Google Play Store.
''')
    button(update, context)



def Native_Android_Apps_Development(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''At our core, we are not confined to smartphones alone. Our prowess in Android mobile app development transcends boundaries, showcasing our mastery across an array of Android devices and platforms. Embracing the full spectrum of possibilities, we have delved deep into the Android realm, leaving no stone unturned. From smartphones to tablets, from Android Wear to Android TV, we fearlessly explore every avenue. Armed with a battle-tested tech stack, our ingenious Android app developers craft apps that mesmerize users and surpass the million-download mark on the prestigious Google Play Store. Prepare to witness the epitome of innovation as we redefine the boundaries of custom Android app development.
''')
    button(update, context)

    



#Talent_acquisition dropdown
def Talent_acquisition(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Altezzasys Offering on Demand Services Ranging from staffing to consulting and many more.
Altezzasys provide these services in Talent Acqusition:
1./SAP_Consulting_Development_Services
2./Staff_Augmentation
3./Cloud_Transformation 
4./Credit_Rating 
5./International_Organization
''')
    

def SAP_Consulting_Development_Services(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Digital technologies are acting as forces to create exponential shifts to multiple dimensions of businesses whether it is organizational, technical or cultural. Lack of a digital strategy has become the biggest roadblock to modernization for companies and industries.
Businesses that are looking to gain a competitive advantage on every touchpoint, aiming to scale business through digital channels and meet client demands through new SAP digital technologies can shape their company’s future by AltezzaSys’s expertise in driving innovation and digital transformation with SAP.
''')
    button(update, context)



def Staff_Augmentation(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''The AltezzaSys is a leading talent advisory and solutions company. We are driven by a powerful purpose – making the future work for everyone. Our services help people fulfil – and exceed – their potential, building employability and connecting people with opportunities. Our solutions enable our clients to optimize their talent needs and organizational models to achieve their goals. While our advocacy and firm commitment to operating responsibly aims to build a better world of work for all.
''')
    button(update, context)



def Cloud_Transformation(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''We Work At The Intersection Of Domain, Data And Technology To Move Your Applications And Data Platforms To The Cloud So That You Can Harness The Power Of Cloud Computing.
''')
    button(update, context)



def Credit_Rating(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''At AltezzaSys, we aim to build new-age EdTech solutions that go beyond conventional online classes and introduce the concept of immersive, interactive, and safe learning. We help educational institutions leverage digital technologies to enhance the quality of learning for students while increasing staff productivity with future-proof automation solutions and online proctoring services. We also offer product engineering services to edu-tech startups and other players in the value chain to accelerate product development and increase speed to market. A precise understanding of the growing challenges and use cases of technologies like extended reality surrounding digital learning has enabled us to help several educational institutions to become state-of-the-art, knowledge-imparting ecosystems of tomorrow.
''')
    button(update, context)



def International_Organization(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''AltezzaSys solutions span across Administrative IT, Program Delivery, Innovation and Digital Transformation needs. Sustainable Development Goals (SDGs) form the core of AltezzaSys’ service offerings and the projects delivered by AltezzaSys reflect the vision of UN and International Organizations. Emergency preparedness solutions, elearning platforms with concurrent massive global access, SEO compliant websites and light portals with high click through rate for global aid, and data management solutions are just some of the speciality solutions offered by AltezzaSys for international organizations, non-profit organizations, and their affiliates.
AltezzaSys partners with banking and financial services institution across the globe to offer a wide portfolio of products and services and help them stay competitive by embracing digital transformation and digital culture.
''')
    button(update, context)















                             



                             












































































#buttonmethod
def button(update, context):
    keyboard = [[InlineKeyboardButton("Yes", callback_data='yes'),
                 InlineKeyboardButton("No", callback_data='no')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Wanna know more?', reply_markup=reply_markup)

def button_callback(update, context):
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == 'yes':
        context.bot.send_message(chat_id=user_id, text="Please enter your mail ID to proceed further:")
        context.user_data['user_id'] = update.effective_user.id
        
        #custom_user_id_counter += 1
        return "AWAITING_EMAIL"
    elif query.data == 'no':
        context.bot.send_message(chat_id=user_id, text="Thank you for Visiting!")
        return ConversationHandler.END

def is_valid_email(email):
    # Email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def email(update, context):
    user_id = context.user_data['user_id']
    
    user_input = update.message.text.strip()
    
   


    if not is_valid_email(user_input):
        update.message.reply_text("Invalid email address. Please enter a valid email.")
        return  # Return without proceeding if the email is invalid
    
    # Save user email to the database
    conn = mysql.connector.connect(**db_config)
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (user_id, email) VALUES (%s, %s)",
                       (user_id, user_input,))
        
        print(cursor.statement)
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        if err.errno == 2055:  # Check if the error is "Cursor is not connected"
            print("Reconnecting to the database...")
            conn.reconnect()  # Reconnect the database
            email(update, context)  # Retry executing the query
        else:
            print("Error while saving email to the database.")
    finally:
        conn.close()
    update.message.reply_text("Email saved successfully! Please enter your Country:")
    return AWAITING_COUNTRY



def save_country(update,context):
    conn = mysql.connector.connect(**db_config)
    user_id = context.user_data['user_id']
    user_input = update.message.text
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET country = %s WHERE user_id = %s", (user_input, user_id))
        conn.commit()
        
        
        update.message.reply_text("Country has been saved successfully.")
        update.message.reply_text("Please provide your contact No.")
    except mysql.connector.Error as err:
        update.message.reply_text("An error occurred while saving the country.")
        print("An error occurred while saving country:", err)
    finally:
        conn.close()
    return AWAITING_CONTACT

def is_valid_contact(contact):
    # Contact number regex pattern (example: +91-1234567890)
    pattern = r'^\d{10}$'
    return re.match(pattern, contact)

def contact(update, context):
    user_id = context.user_data['user_id']
    print(f"Received message from user ID: {user_id}")
    user_input = update.message.text
    
    if not is_valid_contact(user_input):
        update.message.reply_text("Invalid contact number. Please enter a valid contact number in the format: +91-XXXXXXXXXX")
        return 
    # Save user contact to the database
    conn = mysql.connector.connect(**db_config)
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET contact = %s WHERE user_id = %s", (user_input, user_id,))
        admin_user_id = 479960624  # Replace with the actual user ID of the admin
        admin_notification_message = f"User with ID {user_id} saved their contact: {user_input}"
        context.bot.send_message(chat_id=admin_user_id, text=admin_notification_message)
        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        if err.errno == 2055:  # Check if the error is "Cursor is not connected"
            print("Reconnecting to the database...")
            conn.reconnect()  # Reconnect the database
            contact(update, context)  # Retry executing the query
        else:
            print("Error while saving contact to the database.")
    finally:
        conn.close()
        start_button = KeyboardButton("/Start")
        help_button = KeyboardButton("/help")

    # Create a reply keyboard with the "/Start" button
    reply_keyboard = [[start_button], [help_button]]
    update.message.reply_text("Data saved successfully! Our team will connect with you soon.\n"
                              "If you have any queries, please call our helpline: +91-120-4542476",
                             reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    # End the conversation
    context.user_data.clear()
    return ConversationHandler.END













# Command handler for /help command
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm here to help! If you have any questions or need assistance, feel free to ask.")

# Echo handler to respond to user messages


def main():
    # Create an instance of the Updater class
    updater = Updater(TOKEN,use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Store the connection and cursor in the chat_data attribute of the dispatcher

    create_database()
    create_users_table()
    

    # Register the email_callback handler with the dispatcher
    

    # Register command handlers
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    Blockchain_handler = CommandHandler('Blockchain',Blockchain)
    AI_ML_handler = CommandHandler('AI_ML',AI_ML)
    Web_Dev_handler = CommandHandler('Web_Dev',Web_Dev)
    Mobile_Apps_handler = CommandHandler('Mobile_Apps', Mobile_Apps)
    Talent_acquisition_handler = CommandHandler('Talent_acquisition',Talent_acquisition)



    #blockchainhandler
    Metaverse_Development_handler = CommandHandler('Metaverse_Development',Metaverse_Development)
    Uniswap_Clone_Development_handler = CommandHandler('Uniswap_Clone_Development',Uniswap_Clone_Development)
    Smart_Contracts_Development_handler = CommandHandler('mart_Contracts_Development',Smart_Contracts_Development)
    Smart_Contracts_Audit_handler = CommandHandler('Smart_Contracts_Audit',Smart_Contracts_Audit)
    Blockchain_DApps_handler = CommandHandler('Blockchain_DApps',Blockchain_DApps)
    Dex_Development_handler = CommandHandler('Dex_Development',Dex_Development)
    DAO_Development_handler = CommandHandler('DAO_Development',DAO_Development)
    DeFi_Development_handler = CommandHandler('DeFi_Development',DeFi_Development)
    ICO_Launchpads_handler = CommandHandler('ICO_Launchpads',ICO_Launchpads)
    IDO_Launchpads_handler = CommandHandler('IDO_Launchpads',IDO_Launchpads)
    Centralized_Exchange_handler = CommandHandler('Centralized_Exchange',Centralized_Exchange)
    Cryptocurrency_Development_handler = CommandHandler('Cryptocurrency_Development',Cryptocurrency_Development)
    NFT_Marketplace_Development_handler = CommandHandler('NFT_Marketplace_Development',NFT_Marketplace_Development)
    Pancakeswap_Clone_Development_handler = CommandHandler('Pancakeswap_Clone_Development',Pancakeswap_Clone_Development)
    Crypto_Bots_Develop_handler = CommandHandler('Crypto_Bots_Develop',Crypto_Bots_Develop)


    #aimlhandler
    Generative_AI_Services_handler = CommandHandler('Generative_AI_Services',Generative_AI_Services)
    AI_Consulting_handler = CommandHandler('AI_Consulting',AI_Consulting)
    Data_Science_Consulting_handler = CommandHandler('Data_Science_Consulting',Data_Science_Consulting)
    Machine_Learning_handler = CommandHandler('Machine_Learning',Machine_Learning)
    Computer_Vision_handler = CommandHandler('Computer_Vision',Computer_Vision)
    Natural_Language_Processing_handler = CommandHandler('Natural_Language_Processing',Natural_Language_Processing)
    Robotics_Process_Automation_handler = CommandHandler('Robotics_Process_Automation',Robotics_Process_Automation)
    Predictive_Analysis_handler = CommandHandler('Predictive_Analysis',Predictive_Analysis)

    #webdevhandler
    Website_Development_handler = CommandHandler('Website_Development',Website_Development)
    Web_Apps_Development_handler = CommandHandler('Web_Apps_Development',Web_Apps_Development)
    SAAS_Development_handler = CommandHandler('SAAS_Development',SAAS_Development)
    Shopify_Development_handler = CommandHandler('Shopify_Development',Shopify_Development)
    WordPress_Deveopment_handler = CommandHandler('WordPress_Deveopment',WordPress_Deveopment)
    MEAN_MERN_Stack_handler = CommandHandler('MEAN_MERN_Stack',MEAN_MERN_Stack)

    #mobilehandlers
    Native_IOS_Apps_Development_handler = CommandHandler('Native_IOS_Apps_Development',Native_IOS_Apps_Development)
    ARVR_Apps_handler = CommandHandler('ARVR_Apps',ARVR_Apps)
    Progressive_Web_Apps_Development_handler = CommandHandler('Progressive_Web_Apps_Development',Progressive_Web_Apps_Development)
    Flutter_Apps_Development_handler = CommandHandler('Flutter_Apps_Development',Flutter_Apps_Development) 
    React_Native_Apps_Development_handler = CommandHandler('React_Native_Apps_Development',React_Native_Apps_Development)
    Native_Android_Apps_Development_handler = CommandHandler('Native_Android_Apps_Development',Native_Android_Apps_Development)

    #talentaqhandlers
    SAP_Consulting_Development_Services_handler = CommandHandler('SAP_Consulting_Development',SAP_Consulting_Development_Services)
    Staff_Augmentation_handler = CommandHandler('Staff_Augmentation',Staff_Augmentation)
    Cloud_Transformation_handler = CommandHandler('Cloud_Transformation',Cloud_Transformation)
    Credit_Rating_handler = CommandHandler('Credit_Rating',Credit_Rating)
    International_Organization_handler = CommandHandler('International_Organization',International_Organization)


    #messagehandler

    
    
    
   
































































    dispatcher.add_handler(CallbackQueryHandler(button_callback))


    

    # Add the ConversationHandler to the dispatcher
    

    dispatcher.add_handler(CallbackQueryHandler(button))
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text & ~Filters.command, email)],
        states={
            AWAITING_EMAIL: [MessageHandler(Filters.text & ~Filters.command, email)],
            AWAITING_COUNTRY:[MessageHandler(Filters.text & ~Filters.command, save_country)],
            AWAITING_CONTACT: [MessageHandler(Filters.text & ~Filters.command, contact)],
        },
        fallbacks=[],
    )

    dispatcher.add_handler(conv_handler)
    

    
    

    
    
    














    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(Blockchain_handler)
    dispatcher.add_handler(AI_ML_handler)
    dispatcher.add_handler(Web_Dev_handler)
    dispatcher.add_handler(Mobile_Apps_handler)
    dispatcher.add_handler(Talent_acquisition_handler)
    

    #blockchaindispatcher
    dispatcher.add_handler(Metaverse_Development_handler)
    dispatcher.add_handler(Uniswap_Clone_Development_handler)
    dispatcher.add_handler(Smart_Contracts_Development_handler)
    dispatcher.add_handler(Smart_Contracts_Audit_handler)
    dispatcher.add_handler(Blockchain_DApps_handler)
    dispatcher.add_handler(Dex_Development_handler)
    dispatcher.add_handler(DAO_Development_handler)
    dispatcher.add_handler(DeFi_Development_handler)
    dispatcher.add_handler(ICO_Launchpads_handler)
    dispatcher.add_handler(IDO_Launchpads_handler)
    dispatcher.add_handler(Centralized_Exchange_handler)
    dispatcher.add_handler(Cryptocurrency_Development_handler)
    dispatcher.add_handler(NFT_Marketplace_Development_handler)
    dispatcher.add_handler(Pancakeswap_Clone_Development_handler)
    dispatcher.add_handler(Crypto_Bots_Develop_handler)
    

    #aimldispatcher
    dispatcher.add_handler(Generative_AI_Services_handler)
    dispatcher.add_handler(AI_Consulting_handler)
    dispatcher.add_handler(Data_Science_Consulting_handler)
    dispatcher.add_handler(Machine_Learning_handler)
    dispatcher.add_handler(Computer_Vision_handler)
    dispatcher.add_handler(Natural_Language_Processing_handler)
    dispatcher.add_handler(Robotics_Process_Automation_handler)
    dispatcher.add_handler(Predictive_Analysis_handler)
    


    #webdevdispatcher
    dispatcher.add_handler(Website_Development_handler)
    dispatcher.add_handler(Web_Apps_Development_handler)
    dispatcher.add_handler(SAAS_Development_handler)
    dispatcher.add_handler(Shopify_Development_handler)
    dispatcher.add_handler(WordPress_Deveopment_handler)
    dispatcher.add_handler(MEAN_MERN_Stack_handler)
    

    #mobiledispatcher
    dispatcher.add_handler(Native_IOS_Apps_Development_handler)
    dispatcher.add_handler(ARVR_Apps_handler)
    dispatcher.add_handler(Progressive_Web_Apps_Development_handler)
    dispatcher.add_handler(Flutter_Apps_Development_handler)
    dispatcher.add_handler(React_Native_Apps_Development_handler)
    dispatcher.add_handler(Native_Android_Apps_Development_handler)


    #talentdispatcher
    dispatcher.add_handler(SAP_Consulting_Development_Services_handler)
    dispatcher.add_handler(Staff_Augmentation_handler)
    dispatcher.add_handler(Cloud_Transformation_handler)
    dispatcher.add_handler(Credit_Rating_handler)
    dispatcher.add_handler(International_Organization_handler)




    





    



    








































    # Register echo handler for all messages
    

    # Start the bot
    updater.start_polling()
    logger.info("Bot started.")

    # Run the bot until you press Ctrl-C
    updater.idle()




if __name__ == '__main__':
    main()
