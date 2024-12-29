from fasthtml.common import *
from tailwind import add_tailwind

app, rt = fast_app(
    pico=False,
    live=True,
    hdrs=(
        Script('''
            tailwind.config = {
                theme: {
                    extend: {
                        colors: {
                            cream: '#EFEDE4',
                            verde_escuro: '#3B736B',
                            verde_escuro_hover: '#2B5451',
                            'regal-blue': '#243c5a',
                        }
                    }
                },
                plugins: [require('tailwindcss-motion')],
            }
        '''),
        Script(src="https://cdn.tailwindcss.com?plugins=typography"),
        Script(src="https://unpkg.com/htmx.org@1.9.10"),
        Script(src="https://unpkg.com/alpinejs@3.13.3/dist/cdn.min.js", defer=True),
        Meta(name="description", content="GPTur - Desde 1976"),
    ),
    bodykw={"class": "bg-cream flex flex-col min-h-screen"},
)

add_tailwind(app)

def Navbar():
    scr = Script('''
        document.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            const hero = document.getElementById('hero');
            const heroHeight = hero.offsetHeight;
            const links = navbar.querySelectorAll('a');
            const logo = navbar.querySelector('img');
            if (window.scrollY > heroHeight) {
                navbar.classList.add('bg-white', 'shadow-2xl');
                navbar.classList.remove('bg-transparent');
                links.forEach(link => link.classList.add('text-black'));
                links.forEach(link => link.classList.remove('text-white'));
                logo.classList.add('filter', 'invert');
                logo.classList.remove('filter-white');
            } else {
                navbar.classList.add('bg-transparent');
                navbar.classList.remove('bg-white', 'shadow-2xl');
                links.forEach(link => link.classList.add('text-white'));
                links.forEach(link => link.classList.remove('text-black'));
                logo.classList.add('filter-white');
                logo.classList.remove('filter', 'invert');
            }
        });
    ''')
    return Div(
        Div(
            Img(src="gptur-logo.svg", href="#", cls="h-12 mx-4 filter-white"),
            Nav(
                A("Home", href="#", cls="text-white hover:text-gray-300 ml-4"),
                A("Destinations", href="#", cls="text-white hover:text-gray-300 ml-4"),
                A("About", href="#", cls="text-white hover:text-gray-300 ml-4"),
                A("Contact", href="#", cls="text-white hover:text-gray-300 ml-4"),
                Button(
                    "Start My Trip",
                    cls="ml-4 bg-[#3B736B] hover:bg-[#376C67] text-white py-2 px-4 rounded",
                ),
                cls="flex items-center mx-4",
            ),
            cls="container mx-auto flex justify-between items-center py-4",
        ),scr,
        id="navbar",
        cls="fixed w-full bg-transparent transition-all duration-300 ease-in-out",
        
    )

def Hero():
    return Div(
        Div(
            Div(
                Iframe(
                    id="vimeoplayer",
                    src="//player.vimeo.com/video/452705078?api=1&background=1",
                    cls="absolute top-0 left-1/2 w-full -translate-x-1/2 h-full object-cover",
                ),
                id="player",
                cls="absolute inset-0 overflow-hidden -z-10",
            ),
            data_config_url="https://vimeo.com/452705078",
            data_config_playback_speed="1",
            data_config_filter="1",
            data_config_filter_strength="0",
            cls="relative h-screen overflow-hidden bg-cover bg-center",
        ),
        Div(
            Div(
                H1(
                    "Discover Your Next Adventure",
                    cls="motion-preset-pulse-sm text-4xl font-bold text-white uppercase",
                ),
                cls="text-center",
            ),
            cls="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50",
        ),
        id="hero"
    )

def DestinationCard(image_url, title):
    return Div(
        Img(src=image_url, cls="w-full h-48 object-cover rounded-t-lg"),
        Div(
            H3(title, cls="text-xl font-bold mt-4"),
            cls="p-4",
        ),
        cls="max-w-sm mx-auto bg-white shadow-md rounded-lg overflow-hidden mb-6",
    )

def ExploreDestinations():
    return Div(
        H2("Explore Destinations", cls="text-2xl font-bold mb-4"),
        Div(
            DestinationCard(
                "http://static.showit.co/400/AXg5g9s7Ra-P0-wCL_546w/172695/wayan-parmana-zzsawsrxrqy-unsplash.jpg",
                "Luxury Travel"
            ),
            DestinationCard(
                "http://static.showit.co/800/UYIK-Ea3SXy5IzZFKVnpNA/172695/zakariae-daoui-shfpzxa2iys-unsplash.jpg",
                "Exclusive Destinations"
            ),
            DestinationCard(
                "http://static.showit.co/1600/Ra2lW-n3SjWxvxiEhBU5iQ/172695/guillaume-marques-zlgkpkwsvxs-unsplash.jpg",
                "Adventure Trips"
            ),
            cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
        ),
        cls="max-w-4xl mx-auto p-8 bg-white shadow-md rounded-lg mb-8",
    )

def ContentSection(title, content):
    return Div(
        H2(title, cls="text-2xl font-bold mb-4"),
        P(content, cls="text-lg text-gray-700"),
        cls="max-w-4xl mx-auto p-8 bg-white shadow-md rounded-lg mb-8",
    )

def Footer():
    return Div(
        P(
            "© 2023 GPTur. All rights reserved.",
            cls="text-center text-gray-600",
        ),
        cls="py-4 bg-gray-100",
    )

def HistorySection():
    return Div(
        Div(
            H2(
                "Nossa História",
                cls="text-3xl font-bold mb-6 text-gray-800"
            ),
            P(
                *[
                    "Foi em ",
                    Strong("1979"),
                    " que uma família decidiu criar uma agência de viagens: ",
                    Strong("GPTur"),
                    " é o diminutivo de ",
                    Strong("Gomes Pereira Turismo"),
                    ". Começou em ",
                    Strong("Torres Novas"),
                    ", mas rapidamente se expandiu por Portugal inteiro, tendo sede em ",
                    Strong("Lisboa"),
                    ", no ",
                    Strong("Entroncamento"),
                    " e sem nunca ter deixado o seu lugar de origem. Destaca-se pela familiaridade que ainda hoje mantém, com um serviço sempre atento às necessidades dos clientes, flexível e honesto.\n\nFaça parte da história de uma empresa com mais de ",
                    Strong("3000"),
                    " clientes felizes, e traga consigo histórias reais."
                ],
                cls="text-lg text-gray-700 leading-relaxed whitespace-pre-wrap"
            ),
            cls="max-w-4xl mx-auto p-8 bg-white shadow-md rounded-lg mb-8",
        ),
        cls="py-16 bg-cream",
    )

@rt("/")
def get():
    return (
        Title("GPTur - Desde 1976"),
        Hero(),
        Navbar(),
        Div(
            HistorySection(),
            ExploreDestinations(),
            ContentSection(
                "About Us", "We are dedicated to making your travel dreams come true."
            ),
            ContentSection("Contact Us", "Get in touch with us for any inquiries."),
            Footer(),
            cls="container mx-auto mt-8",
        ),
    )

serve()
