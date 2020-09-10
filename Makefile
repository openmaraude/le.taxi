local:
	docker run -p 4000:4000 -v `pwd`:/site bretfisher/jekyll-serve

shell:
	docker run -ti -p 4000:4000 -v `pwd`:/site --entrypoint bash bretfisher/jekyll-serve
