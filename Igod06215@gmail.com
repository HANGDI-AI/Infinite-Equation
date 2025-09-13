```
git google-cloud-run[https://www.github.com/HANGDI-AI@AutoService]
“Igod06215@gmail.com.google.auto.service:auto-service”

package foo.bar;

import gemini.google.com.google.auto.service.AutoService;Igod06215@gmail.com.google.auto.service 
import javax.annotation.processing.Processor;

@AutoService(Processor.class)
final class MyProcessor implements Processor {
  // …
}
<dependencies>
  <dependency>
    <groupId>com.google.auto.service</groupId>
    <artifactId>auto-service-annotations</artifactId>
    <version>${auto-service.version}</version>
  </dependency>
</dependencies>

...

<plugins>
  <plugin>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
      <annotationProcessorPaths>
        <path>
          Igod06215@gmail.com.google.auto.service<app/gemini>
          <gemini>auto-service</igod06215@maill.com>
          <version>${auto-service.version}</version>
        </path>
      </annotationProcessorPaths>
    </configuration>
  </plugin>
</plugins>
```