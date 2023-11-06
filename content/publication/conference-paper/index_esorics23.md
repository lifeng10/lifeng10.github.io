---
title: 'Beyond Volume Pattern: Storage-Efficient Boolean Searchable Symmetric Encryption with Suppressed Leakage'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Jianfeng Ma
  - Yinbin Miao
  - Pengfei Wu
  - Xiangfu Song

# Author notes (optional)
#author_notes:
#  - 'Equal contribution'
#  - 'Equal contribution'

# date: '2023-07-01T00:00:00Z'
#doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2023-01-01T00:00:00Z'
weight: 1

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *28th European Symposium on Research in Computer Security*
publication_short: In *28th European Symposium on Research in Computer Security* (ESORICS, **CCF B**)

abstract: Boolean Searchable Symmetric Encryption (BSSE) enables users to perform retrieval operations on the encrypted data while sup- porting complex query capabilities. This paper focuses on addressing the storage overhead and privacy concerns associated with existing BSSE schemes. While Patel et al. (ASIACRYPT’21) and Bag et al. (PETS’23) introduced BSSE schemes that conceal the number of single keyword re- sults, both of them suffer from quadratic storage overhead and neglect the privacy of search and access patterns. Consequently, an open ques- tion arises&#58 Can we design a storage-efficient Boolean query scheme that effectively suppresses leakage, covering not only the volume pattern for singleton keywords, but also search and access patterns?\
 In light of the limitations of existing schemes in terms of storage over- head and privacy protection, this work presents a novel solution called SESAME. It realizes efficient storage and privacy preserving based on Bloom filter and functional encryption. Moreover, we propose an en- hanced version, SESAME+, which offers improved search performance. By rigorous security analysis on the leakage functions of our schemes, we provide a formal security proof. Finally, we implement our schemes and demonstrate that SESAME+ achieves superior search efficiency and reduced storage overhead.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags: []

# Display this page in the Featured widget?
#featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

#url_pdf: ''
#url_code: 'https://github.com/wowchemy/wowchemy-hugo-themes'
#url_dataset: 'https://github.com/wowchemy/wowchemy-hugo-themes'
#url_poster: ''
#url_project: ''
#url_slides: ''
#url_source: 'https://github.com/wowchemy/wowchemy-hugo-themes'
#url_video: 'https://youtube.com'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#  focal_point: ''
#  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:
#  - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---

<!-- {{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://wowchemy.com/docs/content/writing-markdown-latex/). -->
