import java.io.File;

PImage garImg;
int y;
long count = 0;

void setup() {
  size(800, 480);
  readImagesPath(""); //Must put the path of your image input directory
}

void draw() {
  exit();
}

void readImagesPath(String dir) {
  File folder = new File(dir);
  File[] listOfFiles = folder.listFiles();

    for (File file : listOfFiles) {
    if (file.isFile()) {
      System.out.println(file.getName());

      boolean err = false;

      try {
        garImg = loadImage(file.toString());
      }
      catch(Exception e) {
        err = true;
        System.out.println(e);
      }

      if (!err)
      {
        if (file.getName().contains(".png"))
        {
          //image processing
          background(255);
          int imgWidth = garImg.width;
          int imgHeight = garImg.height;

          if (imgWidth - 800 > imgHeight - 480)
          {
            imgWidth = 800;
            imgHeight = imgHeight * (1 - ((imgWidth - 800) / imgWidth));

            if (imgHeight > 480)
            {
              imgWidth = (1 - ((imgHeight - 480) / imgHeight)) * imgWidth; 
              imgHeight = 480;
            }

            image(garImg, 0, (480 - imgHeight) / 2, imgWidth, imgHeight);
          } else
          {
            imgHeight = 480;
            imgWidth = imgWidth * (1 - ((imgHeight - 480) / imgHeight));

            image(garImg, (800 - imgWidth) / 2, 0, imgWidth, imgHeight);
          }

          loadPixels();
          boolean isImg = false;
          for (int i = 0; i < (width*height)-width; i++) 
          {
            
            if (brightness(pixels[i]) > 100)
            {
              pixels[i] = color(255);
            } else
            {
              pixels[i] = color(0);
              isImg = true;
            }
          }
          updatePixels();

          if (isImg)
          {
            String exportLocation = "export/" + count + ".jpg";

            count++;

            save(exportLocation);
          }
          else
          {
           println("Bad Image File, Skipping"); 
          }
        }
      }
    } else
    {
      readImagesPath(file.toString());
    }
  }
}
