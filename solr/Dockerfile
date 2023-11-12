FROM solr:9.2.1

# For remote JVM debug
EXPOSE 5005
ENV SOLR_OPTS "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005"
