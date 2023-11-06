---
title: "Verifiable and Dynamic Multi-keyword Search over Encrypted Cloud Data Using Bitmap"
authors:
- admin
- Jianfeng Ma
- Yinbin Miao
- Qi Jiang
- Ximeng Liu
- Kim-Kwang Raymond Choo
#author_notes:
#- "Equal contribution"
#- "Equal contribution"
#date: "2021"
doi: "10.1109/TCC.2021.3093304"
weight: 1

# Schedule page publish date (NOT publication's date).
publishDate: "2021-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Transactions on Cloud Computing* (TCC, **CCF C, SCI 2**)"
publication_short: ""

abstract: Searchable Symmetric Encryption (SSE), which enables users to search over encrypted data without decryption, has gained increasing attention from both academic and industrial fields. However, existing SSE schemes either have low search efficiency or cannot support multi-keyword search, dynamic updates, and result verification simultaneously. To solve these problems, we propose a Verifiable and Dynamic Multi-keyword Search (VDMS) scheme over encrypted data by using the bitmap and RSA accumulator, which provides multi-keyword search over encrypted data in an efficient, verifiable and updated way. The bitmap is used as a data structure to build the indexes, which improves the search efficiency and reduces the storage space of the indexes. The RSA accumulator and bitmap are combined to verify the correctness of results. Formal security analysis proves that our VDMS is adaptively secure against Chosen-Keyword Attacks (CKA), and empirical experiments using a real-world dataset demonstrate that our VDMS is efficient and feasible in practical applications.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#tags:
#- Source Themes
#featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://ieeexplore.ieee.org/abstract/document/9470943'
#url_code: ''
#url_dataset: ''
#url_poster: ''
#url_project: ''
#url_slides: ''
#url_source: ''
#url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
#  focal_point: ""
#  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---

<!-- {{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://wowchemy.com/docs/content/writing-markdown-latex/). -->
