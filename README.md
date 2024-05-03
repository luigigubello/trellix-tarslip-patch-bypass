# trellix-tarslip-patch-bypass

In 2023, Trellix announced [1] that they patched +61,000 open-source projects for [CVE-2007-4559](https://nvd.nist.gov/vuln/detail/CVE-2007-4559), an old path traversal vulnerability. Analyzing their patch, it's easy to notice that it can be bypassed using a symlink.

Symlink path traversal is an old technique, and it has also been shown in LiveOverflow's video [ Critical .zip vulnerabilities? - Zip Slip and ZipperDown](https://www.youtube.com/watch?v=Ry_yb5Oipq0).

[1] [Trellix Advanced Research Center Patches 61,000 Vulnerable Open-Source Projects](https://www.trellix.com/blogs/research/trellix-advanced-research-center-patches-vulnerable-open-source-projects/)

### PoC

```
docker build -t tarslip . 
docker run -it tarslip bash
python poc.py
cat evil.txt
```
