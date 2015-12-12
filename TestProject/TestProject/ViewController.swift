//
//  ViewController.swift
//  TestProject
//
//  Created by Luke Solomon on 11/3/15.
//  Copyright © 2015 Luke Solomon. All rights reserved.
//

import UIKit
import Alamofire

class ViewController: UIViewController {

    @IBOutlet weak var tableView: UITableView!
    var responseArray = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.getRequestToApi()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func getRequestToApi () {
        
        Alamofire.request(.GET, "" , parameters: nil)
            .responseJSON { response in

                if let JSON = response.result.value {
                    
                    self.responseArray = (JSON.objectForKey("response"))! as! NSArray
                    
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
        
        print(responseArray)
        print(responseArray.objectAtIndex(indexPath.row))
        print(responseArray.objectAtIndex(indexPath.row) as! [String:AnyObject])
        
        var currentDict:Dictionary = responseArray.objectAtIndex(indexPath.row) as! [String:AnyObject]
        let cellString:String = currentDict["name"] as! String
        
        cell.labelString = cellString
 
        return cell;
    }
    
}
