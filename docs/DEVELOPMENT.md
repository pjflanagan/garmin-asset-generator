
# Development

This is a guide for doing development on Garmin apps, not for how to develop within this repo

## Run

Go to `Run > Run without debugging` then select the device to run on.
Note: the device selection comes up every time because we have a `.vscode/launch.json` file present.

## Adding Fonts

Font info: https://jeffchen.dev/posts/Garmin-Watch-Faces-Custom-Fonts-On-MacOS/

Use this tool
- https://garmin.watchfacebuilder.com/bitmap-font-online-generator/

<!-- 1. Find a font
2. Go on https://snowb.org 
3. Set the text color to white, set the font size, and characters needed (copy from the filter in `fonts.xml`)
4. Click "Export"
5. Name the file using this pattern: `fontName-fontWeight-size`
6. Copy over the `png` and corresponding `fnt` file -->

## Export

Exporting the project for dev and prod release follow similar steps

1. Update the version and environment in `source/CyberpunkComplications.mc`
  - Set the `ENVIRONMENT` to be either `dev` or anything else for prod (but you should use `prod`)
  - Increment the `VERSION` number using this pattern: `<prodRelease>.<devRelease>`, this should preferably align with Garmin's internal version tracking numbers
2. Copy and paste the correct App UUID from `ENVIRONMENTS.md` into `manifest.xml`
  - prod: ensure that all the correct devices are enabled (check `DEVICES.md`)
3. Run `Monkey C: Export Project`
4. Upload to the [Developer Dashboard](https://apps.garmin.com/developer/dashboard) and paste the version number

## Error Reporting

Run `Monkey C: Open ERA Viewer` to see error logs.

## Resources

- [Custom font Making](https://snowb.org/)
- [Custom Font Adding](https://jeffchen.dev/posts/Garmin-Watch-Faces-Custom-Fonts-On-MacOS/)
- [Weather Icons](https://lucide.dev/icons/)
- [Moon Icons](https://erikflowers.github.io/weather-icons/)
- [6-Bit Color Pallet](https://www.flanny.app/6-bit-color-wheel/)
- [SDK Guide](https://developer.garmin.com/connect-iq/api-docs/index.html)
- [Garmin Screen Sizes](https://developer.garmin.com/connect-iq/compatible-devices/)

## Free Version

- This repo is being used to expand on the free version of the app found in this branch: `garmin_cyberpunk_watch_face-FREE-FINAL`
