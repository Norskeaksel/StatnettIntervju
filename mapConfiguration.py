c={
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "Historic Covid Data"
          ],
          "id": "686ha9ug9",
          "name": [
            "Date"
          ],
          "type": "timeRange",
          "value": [
            1579651200000,
            1580823275000
          ],
          "enlarged": True,
          "plotType": "histogram",
          "animationWindow": "free",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "65aoyq6",
          "type": "geojson",
          "config": {
            "dataId": "Historic Covid Data",
            "label": "Historic Covid Data",
            "color": [
              227,
              26,
              26
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": None,
              "colorRange": {
                "name": "Uber Viz Diverging 1.5",
                "type": "diverging",
                "category": "Uber",
                "colors": [
                  "#00939C",
                  "#5DBABF",
                  "#BAE1E2",
                  "#F8C0AA",
                  "#DD7755",
                  "#C22E00"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                104.2
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": {
              "name": "Confirmed",
              "type": "integer"
            },
            "radiusScale": "sqrt"
          }
        },
        {
          "id": "9qi57u7",
          "type": "geojson",
          "config": {
            "dataId": "Last Covid Data",
            "label": "Last Covid Data",
            "color": [
              255,
              153,
              31
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                241,
                92,
                23
              ],
              "colorRange": {
                "name": "Uber Viz Diverging 1.5",
                "type": "diverging",
                "category": "Uber",
                "colors": [
                  "#00939C",
                  "#5DBABF",
                  "#BAE1E2",
                  "#F8C0AA",
                  "#DD7755",
                  "#C22E00"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "Confirmed",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "Historic Covid Data": [
              {
                "name": "Country",
                "format": None
              },
              {
                "name": "Confirmed",
                "format": None
              },
              {
                "name": "Deaths",
                "format": None
              },
              {
                "name": "Date",
                "format": None
              }
            ],
            "Last Covid Data": [
              {
                "name": "Country",
                "format": None
              },
              {
                "name": "Confirmed",
                "format": None
              },
              {
                "name": "Deaths",
                "format": None
              },
              {
                "name": "Date",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 47.53652893009605,
      "longitude": 13.406671920703047,
      "pitch": 0,
      "zoom": 2.516498424956015,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}