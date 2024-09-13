import os
from urllib.parse import urljoin
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def generate_sitemap(base_url, directory):
    urlset = Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                url = SubElement(urlset, 'url')
                loc = SubElement(url, 'loc')
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                full_url = urljoin(base_url, relative_path.replace('\\', '/'))
                loc.text = full_url
                count += 1
    
    xml_string = minidom.parseString(tostring(urlset)).toprettyxml(indent='  ')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_string)
    
    return count

if __name__ == '__main__':
    base_url = 'https://www.bio-hackers.com/'
    directory = '.'  # Current directory, change if needed
    try:
        url_count = generate_sitemap(base_url, directory)
        print(f"Sitemap generated successfully with {url_count} URLs!")
        print("Test run completed.")  # Add this line
    except Exception as e:
        print(f"Error generating sitemap: {str(e)}")
        exit(1)