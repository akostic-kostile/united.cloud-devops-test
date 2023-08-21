FROM debian:11.7-slim as build

RUN apt-get update && apt-get install --yes --no-install-recommends python3 python3-venv

RUN mkdir -p /app/db
WORKDIR /app

## Activate venv, the old fashioned way
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"
## Copy and install reqs so they can be cached independently of the source code
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt && rm -rf requirements.txt

COPY geo_ip.py .
## Run linting to make sure script is PEP8 compliant
RUN pylint geo_ip.py || { echo "Script failed pylint! Exiting." && exit 1; }


FROM gcr.io/distroless/python3-debian11:nonroot as runtime

COPY --chown=65532:65532 --from=build /app /home/nonroot/
USER 65532
WORKDIR /home/nonroot/

ENTRYPOINT [ "/home/nonroot/venv/bin/python3" ]
CMD ["geo_ip.py"]
