//
//  ViewController.m
//  MixPlay
//
//  Created by mccRee on 2019/8/13.
//  Copyright © 2019 PingLang. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    CustomView *cv = [[CustomView alloc]init];
    cv.frame = CGRectMake(100, 100, 100, 100);
    cv.backgroundColor = [UIColor redColor];
    [self.view addSubview:cv];
    [cv changeColor];
}


- (void)helloWorld{
    
}

- (void)checkLogin{
    
}
@end
