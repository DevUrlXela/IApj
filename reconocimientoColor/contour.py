import cv2
#import open cv
import numpy as np
#import numpy for scientific calculations
from matplotlib import pyplot as plt
#display the image

matriz = [[[226 119]], [[225 120]], [[219 120]], [[218 121]], [[215 121]], [[213 123]], [[213 124]], [[212 125]], [[212 147]], [[213 148]], [[213 152]], [[214 153]], [[214 155]], [[215 156]], [[215 157]], [[216 158]], [[216 159]], [[217 160]], [[217 161]], [[218 162]], [[218 163]], [[219 164]], [[219 165]], [[225 171]], [[226 171]], [[227 172]], [[228 172]], [[233 177]], [[233 178]], [[234 179]], [[234 180]], [[240 186]], [[240 187]], [[247 194]], [[248 194]], [[257 203]], [[257 204]], [[258 205]], [[258 206]], [[259 207]], [[259 208]], [[261 210]], [[262 210]], [[263 211]], [[264 211]], [[265 212]], [[266 212]], [[267 213]], [[268 213]], [[269 214]], [[270 214]], [[273 217]], [[274 217]], [[276 219]], [[277 219]], [[280 222]], [[281 222]], [[283 224]], [[284 224]], [[286 226]], [[288 226]], [[290 228]], [[292 228]], [[293 229]], [[294 229]], [[295 230]], [[296 230]], [[297 231]], [[298 231]], [[299 232]], [[301 232]], [[302 233]], [[304 233]], [[305 234]], [[307 234]], [[308 235]], [[310 235]], [[311 236]], [[313 236]], [[314 237]], [[315 237]], [[316 238]], [[317 238]], [[318 239]], [[321 239]], [[322 240]], [[325 240]], [[326 241]], [[328 241]], [[329 242]], [[331 242]], [[332 243]], [[334 243]], [[335 244]], [[338 244]], [[339 245]], [[342 245]], [[343 246]], [[346 246]], [[347 247]], [[350 247]], [[351 248]], [[354 248]], [[355 249]], [[359 249]], [[360 250]], [[364 250]], [[365 251]], [[369 251]], [[370 252]], [[375 252]], [[376 253]], [[381 253]], [[382 254]], [[389 254]], [[390 255]], [[405 255]], [[406 256]], [[445 256]], [[446 255]], [[458 255]], [[459 254]], [[466 254]], [[467 253]], [[470 253]], [[471 252]], [[474 252]], [[475 251]], [[477 251]], [[478 250]], [[480 250]], [[481 249]], [[484 249]], [[485 248]], [[486 248]], [[487 247]], [[489 247]], [[490 246]], [[491 246]], [[492 245]], [[495 245]], [[496 244]], [[497 244]], [[498 243]], [[499 243]], [[501 241]], [[503 241]], [[504 240]], [[506 240]], [[507 239]], [[508 239]], [[509 238]], [[510 238]], [[511 237]], [[513 237]], [[514 236]], [[515 236]], [[516 235]], [[517 235]], [[520 232]], [[521 232]], [[522 231]], [[523 231]], [[528 226]], [[529 226]], [[530 225]], [[531 225]], [[540 216]], [[543 216]], [[547 212]], [[547 211]], [[548 210]], [[548 209]], [[550 207]], [[550 206]], [[551 205]], [[551 204]], [[554 201]], [[555 201]], [[556 200]], [[559 200]], [[560 199]], [[561 199]], [[564 196]], [[564 195]], [[568 191]], [[568 190]], [[569 189]], [[569 188]], [[571 186]], [[571 185]], [[572 184]], [[572 183]], [[573 182]], [[573 181]], [[574 180]], [[574 178]], [[575 177]], [[575 176]], [[576 175]], [[576 173]], [[577 172]], [[577 165]], [[576 164]], [[576 163]], [[572 159]], [[572 158]], [[568 154]], [[568 153]], [[567 152]], [[567 151]], [[565 149]], [[564 149]], [[563 148]], [[562 148]], [[560 146]], [[559 146]], [[558 145]], [[555 145]], [[554 144]], [[552 144]], [[551 143]], [[548 143]], [[547 142]], [[542 142]], [[541 143]], [[538 143]], [[537 144]], [[534 144]], [[533 145]], [[529 145]], [[528 146]], [[525 146]], [[524 147]], [[519 147]], [[518 148]], [[514 148]], [[513 149]], [[508 149]], [[507 150]], [[503 150]], [[502 151]], [[497 151]], [[496 152]], [[493 152]], [[492 153]], [[488 153]], [[487 154]], [[484 154]], [[483 155]], [[479 155]], [[478 156]], [[475 156]], [[474 157]], [[470 157]], [[469 158]], [[464 158]], [[463 159]], [[457 159]], [[456 160]], [[449 160]], [[448 161]], [[439 161]], [[438 162]], [[391 162]], [[390 161]], [[383 161]], [[382 160]], [[374 160]], [[373 159]], [[367 159]], [[366 158]], [[360 158]], [[359 157]], [[356 157]], [[355 156]], [[352 156]], [[351 155]], [[349 155]], [[348 154]], [[346 154]], [[345 153]], [[343 153]], [[342 152]], [[340 152]], [[339 151]], [[338 151]], [[337 150]], [[335 150]], [[334 149]], [[333 149]], [[332 148]], [[330 148]], [[329 147]], [[327 147]], [[326 146]], [[324 146]], [[323 145]], [[322 145]], [[321 144]], [[319 144]], [[318 143]], [[317 143]], [[316 142]], [[315 142]], [[314 141]], [[312 141]], [[311 140]], [[310 140]], [[309 139]], [[307 139]], [[306 138]], [[305 138]], [[304 137]], [[303 137]], [[302 136]], [[300 136]], [[299 135]], [[297 135]], [[296 134]], [[295 134]], [[294 133]], [[292 133]], [[291 132]], [[289 132]], [[288 131]], [[285 131]], [[284 130]], [[283 130]], [[282 131]], [[279 131]], [[276 134]], [[273 134]], [[272 135]], [[271 135]], [[270 134]], [[267 134]], [[266 133]], [[265 133]], [[264 132]], [[263 132]], [[262 131]], [[261 131]], [[252 122]], [[251 122]], [[250 121]], [[247 121]], [[246 120]], [[240 120]], [[239 119]]]

print *"HOLA"