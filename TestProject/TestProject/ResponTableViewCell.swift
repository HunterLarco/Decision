//
//  ResponTableViewCell.swift
//  TestProject
//
//  Created by Luke Solomon on 11/3/15.
//  Copyright © 2015 Luke Solomon. All rights reserved.
//

import UIKit

class ResponseTableViewCell:UITableViewCell {
    
    
    @IBOutlet weak var lukesImageView: UIImageView!
    @IBOutlet weak var label: UILabel!
    
    var labelString:String! {
        didSet{
            self.label.text = labelString
        }
    }
    
    var imageData:NSData!
    
    
    
}