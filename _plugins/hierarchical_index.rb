module Jekyll
  class HierarchicalIndexTag < Liquid::Tag
    def initialize(tag_name, pages, tokens)
      super
      @pages = pages
    end

    def render(context)
      pages = context[@pages]
      result = ""
      previous_section = []
      pages.each do |page|
        url_elements = page.url.split('/').select { |x| x.length > 0 }
        title = url_elements[-1].gsub('_', ' ')
        url = page.url
        # Calculate opening and closing of lists by length of common prefix
        section = url_elements[0...-1]
        common = section.zip(previous_section).take_while { |pair|
            pair[0] == pair[1]
        }
        # Close previous sections
        result += "</ul>"*(previous_section.length - common.length)
        # Open new sections
        result += "<ul>"*(section.length - common.length)
        result += "<li>"
        result += "<a href=\"#{url}\">#{title}</a>\n"
        result += "</li>\n"
        previous_section = section
      end
      result += "</ul>"*previous_section.length
      result
    end
  end
end

Liquid::Template.register_tag('hierarchical_index', Jekyll::HierarchicalIndexTag)

