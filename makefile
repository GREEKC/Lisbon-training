################################################################
## Synchronize web site on the server

################################################################
## Variables
MAKEFILE=makefile
MAKE=make -s -f ${MAKEFILE}
DATE=`date +%Y-%M-%d_%H:%M:%S`
GITHUB_ACCOUNT=GREEKC
GITHUB_REPO=Lisbon-training

################################################################
## List of targets
usage:
	@echo "usage: make [-OPT='options'] target"
	@echo "implemented targets"
	@perl -ne 'if (/^([a-z]\S+):/){ print "\t$$1\n";  }' ${MAKEFILE}


################################################################
## Clean temporary files created by emacs
clean:
	find . -name '*~' -exec rm {} \;
	find . -name '.#*' -exec rm {} \;
	find . -name '.DS_Store' -exec rm {} \;


################################################################
## Print the URL of the github repository
GITHUB_URL=http://github.com/${GITHUB_ACCOUNT}/${GITHUB_REPO}
github:
	@echo "Github site"
	@echo "	${GITHUB_URL}"
	open  ${GITHUB_URL}

################################################################
## Get the URL of the Web site
WEB_URL=http://${GITHUB_ACCOUNT}.github.io/${GITHUB_REPO}
web:
	@echo "Web site"
	@echo "	${WEB_URL}"
	open  ${WEB_URL}

