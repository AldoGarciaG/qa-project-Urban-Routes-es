Test Urban Routes

Descripcion:

Este proyecto busca automatizar las pruebas de la plataforma web Urban Routes, la cual ofrece un servicio para pedir taxis 
a través de una interfaz visual. La meta es automatizar todo el proceso de solicitud de un taxi, incluyendo la elección de 
direcciones, el pago, servicios incluidos en el trayecto y el envío de un mensaje de texto al chofer. 
Además, se busca validar el correcto funcionamiento de cada proceso del sistema, asegurando que la experiencia del usuario 
sea fluida, eficiente y libre de errores durante todo el flujo de interacción.


Tecnologías y Técnicas Utilizadas:

-PyCharm Community Edition 

-Selenium: Herramienta utilizada para controlar y automatizar acciones dentro del navegador web.

-Pytest: Plataforma empleada para organizar y ejecutar pruebas de manera automatizada.

-WebDriver (Google Chrome): Componente que permite simular el comportamiento de un usuario dentro del navegador Chrome.

-XPath Selectors: Método utilizado para localizar con precisión elementos específicos en una página web.

-GitHub: Plataforma de control de versiones y colaboración que permite almacenar, gestionar y compartir el código fuente del proyecto.


Tecnicas Utilizadas:

-Se encapsula toda la lógica de interacción con la interfaz en la clase UrbanRoutesPage, separando la lógica de pruebas en TestUrbanRoutes de la lógica de UI.

-Se usa WebDriverWait combinado con condiciones como presence_of_element_located o element_to_be_clickable, lo cual es clave para pruebas confiables en aplicaciones con carga dinámica.

-Se importa un módulo data para mantener separados los datos de prueba (teléfono, dirección, mensaje, etc.) del código de prueba. Esto mejora la reutilización y legibilidad.


Entorno:

-Asegúrate de tener instalada la versión más reciente de Google Chrome.

-Comprueba que el chromedriver que estás utilizando sea compatible con la versión actual de tu navegador.