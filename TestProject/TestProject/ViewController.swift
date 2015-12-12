//
//  ViewController.swift
//  TestProject
//
//  Created by Luke Solomon on 11/3/15.
//  Copyright © 2015 Luke Solomon. All rights reserved.
//

import UIKit
import Alamofire

let BASEURL:String = "ayy lmao"

class ViewController:UIViewController {

    @IBOutlet weak var tableView:UITableView!
    var responseArray:NSArray = ["Vote", "Ayy lmao"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //self.getRequestToApi()
        
    }
    
    func getRequestToApi () {
        
        Alamofire.request(.GET, "\(BASEURL)" , parameters: nil)
        .responseJSON { response in
            if let JSON = response.result.value {
                
                self.responseArray = (JSON.objectForKey("response"))! as! Array<String>
                
                dispatch_async(dispatch_get_main_queue(), {
                  self.tableView.reloadData()
                })
            }
        }
    }
}

extension ViewController: UITableViewDelegate {
    
}

extension ViewController: UITableViewDataSource {
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return responseArray.count;
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell:ResponseTableViewCell = tableView.dequeueReusableCellWithIdentifier("ResponseCell", forIndexPath: indexPath) as! ResponseTableViewCell
        
//        var currentDict:Dictionary =
        let cellString:String = responseArray.objectAtIndex(indexPath.row) as! String
        
        cell.labelString = cellString
 
        return cell;
    }
    
}
