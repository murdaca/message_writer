# message-writer

Create json file to be used by the WMS server.

1. Build the container
```
docker build -t message-worker .
```

2. create the configuration file
Configuration file for the script has the following information:
  - output file name path, for example `/tmp/list-of-files.json`
  - area file path (taken from https://github.com/pytroll/satpy/blob/main/satpy/etc/areas.yaml)
  - filepattern, for example `/eodata/fci-out/{start_time:%Y%m%d_%H%M}_{platform_name}_{area}_{product}.tif`

Example file called `config_fci.yaml`:
```bash
filename: /tmp/list-of-files.json
area_file:  /usr/local/bin/message-writer/areas.yaml
filepattern: /eodata/fci-out/{start_time:%Y%m%d_%H%M}_{platform_name}_{area}_{product}.tif
```
  
3. Enter interactive mode of the container mounting the `area file`, the `configuration file` (from point 2) and the actual products created with satpy
```
docker run -it -v ./config_fci.yaml:/usr/local/bin/message-writer/config_fci.yaml -v /tmp/:/tmp/ -v /home/murdaca/fci-data/:/eodata/fci-out  message-worker /bin/bash
```

4. run the following command:
```
python3 create_file.py config_fci.yaml /eodata/fci-out/
```

Example output of the json (formatted):

```bash
[
   {
      "uri":"/eodata/fci_out/20231124_1150_MTI1_eurol_airmass.tif",
      "layer":"airmass",
      "start_time":"2023-11-24T11:50:00Z",
      "area_extent":[
         -3780000.0,
         -7644000.0,
         3900000.0,
         -1500000.0
      ],
      "proj4":"+ellps=WGS84 +lat_0=90 +lat_ts=60 +lon_0=0 +no_defs +proj=stere +type=crs +units=m +x_0=0 +y_0=0"
   },
   {
      "uri":"/eodata/fci_out/20231124_1150_MTI1_eurol_cimss_cloud_type.tif",
      "layer":"cimss_cloud_type",
      "start_time":"2023-11-24T11:50:00Z",
      "area_extent":[
         -3780000.0,
         -7644000.0,
         3900000.0,
         -1500000.0
      ],
      "proj4":"+ellps=WGS84 +lat_0=90 +lat_ts=60 +lon_0=0 +no_defs +proj=stere +type=crs +units=m +x_0=0 +y_0=0"
   },
   {
      "uri":"/eodata/fci_out/20231124_1150_MTI1_eurol_cloud_phase.tif",
      "layer":"cloud_phase",
      "start_time":"2023-11-24T11:50:00Z",
      "area_extent":[
         -3780000.0,
         -7644000.0,
         3900000.0,
         -1500000.0
      ],
      "proj4":"+ellps=WGS84 +lat_0=90 +lat_ts=60 +lon_0=0 +no_defs +proj=stere +type=crs +units=m +x_0=0 +y_0=0"
   },
   {
      "uri":"/eodata/fci_out/20231124_1150_MTI1_eurol_fog.tif",
      "layer":"fog",
      "start_time":"2023-11-24T11:50:00Z",
      "area_extent":[
         -3780000.0,
         -7644000.0,
         3900000.0,
         -1500000.0
      ],
      "proj4":"+ellps=WGS84 +lat_0=90 +lat_ts=60 +lon_0=0 +no_defs +proj=stere +type=crs +units=m +x_0=0 +y_0=0"
   },
   {
      "uri":"/eodata/fci_out/20231124_1150_MTI1_eurol_natural_color.tif",
      "layer":"natural_color",
      "start_time":"2023-11-24T11:50:00Z",
      "area_extent":[
         -3780000.0,
         -7644000.0,
         3900000.0,
         -1500000.0
      ],
      "proj4":"+ellps=WGS84 +lat_0=90 +lat_ts=60 +lon_0=0 +no_defs +proj=stere +type=crs +units=m +x_0=0 +y_0=0"
   },
   {
      "uri":"/eodata/fci_out/20231124_1150_MTI1_eurol_night_fog.tif",
      "layer":"night_fog",
      "start_time":"2023-11-24T11:50:00Z",
      "area_extent":[
         -3780000.0,
         -7644000.0,
         3900000.0,
         -1500000.0
      ],
      "proj4":"+ellps=WGS84 +lat_0=90 +lat_ts=60 +lon_0=0 +no_defs +proj=stere +type=crs +units=m +x_0=0 +y_0=0"
   },
   {
      "uri":"/eodata/fci_out/20231124_1150_MTI1_eurol_true_color.tif",
      "layer":"true_color",
      "start_time":"2023-11-24T11:50:00Z",
      "area_extent":[
         -3780000.0,
         -7644000.0,
         3900000.0,
         -1500000.0
      ],
      "proj4":"+ellps=WGS84 +lat_0=90 +lat_ts=60 +lon_0=0 +no_defs +proj=stere +type=crs +units=m +x_0=0 +y_0=0"
   }
]
```
