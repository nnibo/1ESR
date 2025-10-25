const htmlElement = document.querySelector('html')
const btnTheme = document.querySelector('#btn-theme')

btnTheme.addEventListener('click', () => {
    htmlElement.classList.toggle('dark');
}
)