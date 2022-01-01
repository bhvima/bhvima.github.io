--- 
layout: post
title: Functional Programming - Scala
excerpt: Writing code in an entirely functional style without using loops, if-else statements and mutable states.
---

Scala is a multi-paradigm language - a mix of both object oriented and functional styles. Now let us strip the object oriented programming aspect and write code in an entirely functional style. 
Let us even restrict loops, if-else statements and mutable states (no `var` variables). These were the restrictions on a project, I worked on last semester. These artificial hoops were meant to engineer new computing solutions.

The project on a high level involved writing the back-end of a mobile application that rated nearby restaurants using Collaborative filtering.

All input data was provided as comma-separated files (CSV). The first step was to write functions to process multiple CSV files.

```scala
import java.io.File
import scala.io.Source

def parseDir(dir: File): List[Rating] = dir.listFiles.filter(_.isFile).toList.flatMap { file => 
        Source.fromFile(file).getLines().toList.tail.map(_.split(",")).map { value =>
            new Rating(value(0), value(1).toInt, value(4), value(5), value(6).toInt)
        }
    }
```


