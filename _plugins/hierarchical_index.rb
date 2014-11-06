module Jekyll
  class HierarchicalIndexTag < Liquid::Tag
    def initialize(tag_name, pages, tokens)
      super
      @pages = pages
    end

    def common_prefix(a, b)
      prefixed_pairs = a.zip(b).take_while { |pair| pair[0] == pair[1] }
      prefixed_pairs.map { |a, b| a }
    end

    def render(context)
      pages = context[@pages]
      result = ""
      previous_section = []
      all_urls = pages.map { |page| page.url }
      pages.each do |page|
        url_elements = page.url.split('/').select { |x| x.length > 0 }
        title = url_elements[-1].gsub('_', ' ')
        url = page.url
        # Calculate opening and closing of lists by length of common prefix
        section = url_elements[0...-1]
        common = common_prefix(section, previous_section)
        # Close previous sections
        result += "</ul>"*(previous_section.length - common.length)
        # Open new sections
        result += "<ul>"*(section.length - common.length)
        is_opener = all_urls.any? { |page_url|
          page_url != url and page_url.start_with?(url)
        }
        result += "<li>"
        if is_opener then
          result += "<strong>"
        end
        result += "<a href=\"#{url}\">#{title}</a>\n"
        if is_opener then
          result += "</strong>"
        end
        result += "</li>\n"
        previous_section = section
      end
      result += "</ul>"*previous_section.length
      result
    end
  end
end

Liquid::Template.register_tag('hierarchical_index', Jekyll::HierarchicalIndexTag)

