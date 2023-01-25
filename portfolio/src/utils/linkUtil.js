import svelteLogo from '../assets/svelte.svg'

export const navbarData = {
    logo: true,
    logoSrc: svelteLogo,
    logoLink: true,
    linkUrl: '#/',
    optionalLinkText: 'velte spa',
    altText: 'Logo',
    links: [
        {url: '#/Home', displayInNav: true, displayInFooter: true, linkText: 'Home'},
        {url: '#/About', displayInNav: true, displayInFooter: true, linkText: 'About'},
        {url: '#/Contact', displayInNav: true, displayInFooter: true, linkText: 'Contact'},
        {url: '#/Projects', displayInNav: true, displayInFooter: true, linkText: 'Projects'},
    ]
}